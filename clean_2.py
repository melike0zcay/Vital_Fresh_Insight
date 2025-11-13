import os

# Gizli dosyaları bulmak için fonksiyon
def find_hidden_files(directory):
    for foldername in os.listdir(directory):
        folder_path = os.path.join(directory, foldername)
        if os.path.isdir(folder_path):
            find_hidden_files(folder_path)  # Alt klasörleri kontrol et
        else:
            file_path = folder_path
            if foldername.startswith('.'):  # Gizli dosyalar '.' ile başlar
                print(f"Gizli dosya bulundu: {file_path}")

# Gizli dosyaları dataset klasöründe bulalım
dataset_dir = "dataset"
find_hidden_files(dataset_dir)
