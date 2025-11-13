from PIL import Image
import os

# Dataset yolunu belirtin
dataset_dir = "dataset_train"
output_format = "JPEG"  # Tüm resimleri JPEG formatına çevireceğiz

def convert_images_to_jpeg(directory):
    for foldername in os.listdir(directory):
        folder_path = os.path.join(directory, foldername)
        if os.path.isdir(folder_path):
            convert_images_to_jpeg(folder_path)
        else:
            file_path = folder_path
            try:
                with Image.open(file_path) as img:
                    rgb_img = img.convert('RGB')  # Resmi RGB formatına çevir
                    new_file_path = os.path.splitext(file_path)[0] + ".jpg"  # Yeni dosya ismi
                    rgb_img.save(new_file_path, output_format)
                    print(f"Resim dönüştürüldü: {new_file_path}")
            except Exception as e:
                print(f"Resim dönüştürülemedi: {file_path} - {e}")

convert_images_to_jpeg(dataset_dir)
