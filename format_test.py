import os
from PIL import Image

# Dataset yolunu belirtin
dataset_dir = "C:\\Users\\elifmelike\\Melike\\dataset"


# Desteklenen formatlar
ALLOWED_FORMATS = ["PNG", "JPEG"]

def check_image_formats(directory):
    invalid_images = []
    for foldername in os.listdir(directory):
        folder_path = os.path.join(directory, foldername)
        if os.path.isdir(folder_path):
            invalid_images.extend(check_image_formats(folder_path))
        else:
            file_path = folder_path
            try:
                with Image.open(file_path) as img:
                    if img.format not in ALLOWED_FORMATS:
                        invalid_images.append(file_path)
            except Exception as e:
                print(f"Resim kontrol edilemedi: {file_path} - {e}")
    return invalid_images

# Test fonksiyonunu çalıştır
invalid_images = check_image_formats(dataset_dir)

if invalid_images:
    print("Geçersiz formatta olan resimler:")
    for img in invalid_images:
        print(img)
else:
    print("Tüm resimler uygun formatta.")
