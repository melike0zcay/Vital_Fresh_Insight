import os
from PIL import Image

# Klasör yolunu belirtin
dataset_dir = "dataset_test"  # Ana veri seti klasörünüz (Fruits ve Vegetables'ı içeren)

# Desteklenen formatlar
valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']

# Hatalı dosyaları kontrol eden fonksiyon
def check_images(directory):
    for foldername in os.listdir(directory):
        folder_path = os.path.join(directory, foldername)
        if os.path.isdir(folder_path):  # Eğer klasörse
            check_images(folder_path)  # Klasörün içine gir
        else:
            file_path = folder_path
            file_extension = os.path.splitext(file_path)[1].lower()  # Dosya uzantısını al
            if file_extension not in valid_extensions:
                print(f"Geçersiz format: {file_path}")  # Geçersiz formatta dosya
            else:
                try:
                    img = Image.open(file_path)  # Dosyayı açmayı dene
                    img.verify()  # Dosyanın bozuk olup olmadığını kontrol et
                except (IOError, SyntaxError) as e:
                    print(f"Bozuk dosya: {file_path} - {e}")  # Geçerli bir resim dosyası değil

# Klasördeki tüm dosyaları kontrol et
check_images(dataset_dir)

