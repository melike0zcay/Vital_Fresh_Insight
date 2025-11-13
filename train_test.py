import os
import shutil
import random

# Klasör yolları
source_dir = 'dataset'  # Orijinal veri setinizin bulunduğu yer
train_dir = 'dataset_train'  # Train seti için yeni klasör
test_dir = 'dataset_test'    # Test seti için yeni klasör

# Test seti oranı
test_ratio = 0.2  # %20 test, %80 train

# Verileri ayırma fonksiyonu
def split_data(source, train, test, test_ratio):
    for category in os.listdir(source):
        category_path = os.path.join(source, category)
        
        if not os.path.isdir(category_path):  # Klasör olup olmadığını kontrol et
            continue
        
        for class_name in os.listdir(category_path):
            class_path = os.path.join(category_path, class_name)
            if not os.path.isdir(class_path):
                continue
            
            images = os.listdir(class_path)  # Tüm resimleri al
            random.shuffle(images)  # Karıştır
            
            # Ayırma noktası
            split_point = int(len(images) * (1 - test_ratio))
            
            # Train ve test verileri
            train_images = images[:split_point]
            test_images = images[split_point:]
            
            # Yeni klasörler oluştur
            os.makedirs(os.path.join(train, category, class_name), exist_ok=True)
            os.makedirs(os.path.join(test, category, class_name), exist_ok=True)
            
            # Train setine kopyalama
            for image in train_images:
                shutil.copy(os.path.join(class_path, image), os.path.join(train, category, class_name, image))
            
            # Test setine kopyalama
            for image in test_images:
                shutil.copy(os.path.join(class_path, image), os.path.join(test, category, class_name, image))

# Train ve test setlerine ayırma
split_data(source_dir, train_dir, test_dir, test_ratio)

print("Veriler başarıyla train ve test setlerine ayrıldı.")
