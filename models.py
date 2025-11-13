import tensorflow as tf
import os
import matplotlib.pyplot as plt

# Veri kümesi ile ilgili bazı parametreler
batch_size = 32
img_height = 100
img_width = 100

# Train veri setini yükleme
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
  'dataset_train',  # Train seti klasörü
  image_size=(img_height, img_width),
  batch_size=batch_size,
  label_mode='int',  # Klasör isimlerine göre etiketleme yapılacak
  color_mode='rgb',  # Renkli görüntüler için
  shuffle=True,  # Verileri karıştır
  validation_split=0.2,  # Veriyi %80 train, %20 validation olarak ayır
  subset="training",  # Bu kısım "training" verisi
  seed=123  # Karışıklığın her seferinde aynı olmasını sağlamak için sabit bir seed
)

# Validation setini yükleme (test seti olarak da kullanılabilir)
val_ds = tf.keras.preprocessing.image_dataset_from_directory(
  'dataset_train',  # Aynı klasör
  image_size=(img_height, img_width),
  batch_size=batch_size,
  label_mode='int',
  color_mode='rgb',
  shuffle=True,
  validation_split=0.2,  # %80 train, %20 validation olarak ayır
  subset="validation",  # Bu kısım "validation" verisi
  seed=123
)

# Sınıf isimlerini alalım (örneğin: FreshApple, RottenApple, FreshTomato, RottenTomato)
class_names = train_ds.class_names
print("Sınıf isimleri:", class_names)

# Veriyi optimize etmek için cache ve prefetch işlemi uygulayabiliriz
AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

# Modeli oluşturma (CNN - Convolutional Neural Network)
model = tf.keras.Sequential([
    # Piksel değerlerini 0-255 aralığından 0-1 aralığına normalize etmek için
    tf.keras.layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
    
    # Evrişimsel katmanlar
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    
    # Düzleştirme (Flatten) ve Dense (Tam Bağlantılı) katmanlar
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    
    # Son katman: Sınıflandırma için çıktı katmanı
    tf.keras.layers.Dense(len(class_names))  # Sınıf sayısı kadar çıktı (örneğin 4 sınıf)
])


if __name__ == "__main__":
  # Modeli derleme
  model.compile(
      optimizer='adam',
      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
      metrics=['accuracy']
  )
  
  # Modelin özetini görmek için
  model.summary()

  # Modeli eğitme
  epochs = 10  # 10 epoch boyunca eğitelim
  history = model.fit(
      train_ds,
      validation_data=val_ds,  # Doğrulama verisi olarak validation seti kullanılır
      epochs=epochs
  )

  # Eğitimden sonra sonuçları görselleştirme
  acc = history.history['accuracy']
  val_acc = history.history['val_accuracy']
  loss = history.history['loss']
  val_loss = history.history['val_loss']

  epochs_range = range(epochs)

  plt.figure(figsize=(8, 8))
  plt.subplot(1, 2, 1)
  plt.plot(epochs_range, acc, label='Training Accuracy')
  plt.plot(epochs_range, val_acc, label='Validation Accuracy')
  plt.legend(loc='lower right')
  plt.title('Training and Validation Accuracy')

  plt.subplot(1, 2, 2)
  plt.plot(epochs_range, loss, label='Training Loss')
  plt.plot(epochs_range, val_loss, label='Validation Loss')
  plt.legend(loc='upper right')
  plt.title('Training and Validation Loss')
  plt.show()

  # Test seti üzerinde sonuçları değerlendirme (val_ds'i test gibi kullanıyoruz)
  print("\nValidation veri seti üzerinde modelin performansı:")
  test_loss, test_acc = model.evaluate(val_ds)
  print(f'Test Doğruluğu: {test_acc:.2f}')

  model.save('models_c2.h5')  # 'my_model.h5' istediğiniz dosya adıdır
  print("Model başarıyla kaydedildi.")
