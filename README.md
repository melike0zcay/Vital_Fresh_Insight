Vital_Fresh_Insight

Description

This project is a web application that predicts whether fruits and vegetables are fresh or rotten.
The project contains two models:

Google Cloud Model → Used for real predictions, trained on Google Cloud.

My Own Trained Model (model_c2.h5) → Included for demonstration and educational purposes.

Users can upload an image and get predictions in JSON format or view results on the web page.

Features

Classifies fresh vs. rotten fruits and vegetables

Flask-based web interface

Processes user-uploaded images and returns predictions in JSON format

Accurate predictions using the Google Cloud-trained model

Includes code for the user-trained model

Technologies

Python: Programming language

Flask: Web application framework

TensorFlow / Keras: Model loading and prediction

Pillow (PIL): Image processing

NumPy: Numerical computations

HTML / CSS: Web page interface

File Structure
Vital_Fresh_Insight/
app.py                  # Flask app returning JSON (uses Google Cloud model)
app2.py                 # Previous version, for testing user-trained model
model_c2.h5             # User-trained model
converted_savedmodel/   # Google Cloud-trained model
dataset_train/          # Training dataset folder
templates/
    index.html          # Web interface
clean_dataset.py        # Script to clean dataset
convert.py              # Convert images to JPEG format
format_test.py          # Check image formats
README.md               # This file

Dataset

Dataset used in this project:
[“Fruits and Vegetables Dataset” – Kaggle link](https://www.kaggle.com/datasets/muhriddinmuxiddinov/fruits-and-vegetables-dataset)

Installation and Usage

Clone the repo:

git clone https://github.com/melike0zcay/Vital_Fresh_Insight.git
cd Vital_Fresh_Insight


Install required packages:

pip install -r requirements.txt


Run the Flask app:

python app.py


Open http://127.0.0.1:5000
 in your browser and upload an image to get predictions.

Notes

__pycache__ and large model files should generally not be pushed to GitHub

model_c2.h5 → User-trained model, included with training code

converted_savedmodel/ → Google Cloud-trained model, used for real predictions


-----------------------------------------------------------------------------------------

Vital_Fresh_Insight

Açıklama

Bu proje, meyve ve sebzelerin taze mi yoksa çürük mü olduğunu tahmin eden bir web uygulamasıdır.
Projede iki model bulunmaktadır:

Google Cloud Modeli → Gerçek tahminler için kullanılır, Google Cloud üzerinde eğitilmiştir.

Kendi Eğittiğim Model (model_c2.h5) → Eğitim ve gösterim amaçlı eklenmiştir.

Kullanıcılar bir resim yükleyebilir ve tahmini JSON formatında alabilir veya web sayfasında görebilir.

Özellikler

Taze ve çürük meyve/sebzeleri sınıflandırır

Flask tabanlı web arayüzü

Kullanıcı tarafından yüklenen resimleri işler ve JSON formatında tahmin döndürür

Google Cloud modeli ile doğru tahminler

Kullanıcı eğitimi yapılan model için kodu içerir

Teknolojiler

Python: Programlama dili

Flask: Web uygulama çatısı

TensorFlow / Keras: Model yükleme ve tahmin

Pillow (PIL): Görüntü işleme

NumPy: Sayısal hesaplamalar

HTML / CSS: Web sayfası arayüzü

Dosya Yapısı
Vital_Fresh_Insight/
app.py                  # Google Cloud modelini kullanan JSON döndüren Flask uygulaması
app2.py                 # Kullanıcı eğitimi modelini test etmek için eski sürüm
model_c2.h5             # Kullanıcı eğitimi model
converted_savedmodel/   # Google Cloud eğitilmiş model
dataset_train/          # Eğitim veri seti klasörü
templates/
    index.html          # Web arayüzü
clean_dataset.py        # Veri setini temizleyen script
convert.py              # Resimleri JPEG formatına çevirir
format_test.py          # Resim formatlarını kontrol eder
README.md               # Bu dosya

Veri Seti

Projede kullanılan veri seti:
[“Fruits and Vegetables Dataset” – Kaggle linki](https://www.kaggle.com/datasets/muhriddinmuxiddinov/fruits-and-vegetables-dataset)

Kurulum ve Kullanım

Repoyu kopyalayın:

git clone https://github.com/melike0zcay/Vital_Fresh_Insight.git
cd Vital_Fresh_Insight


Gerekli paketleri yükleyin:

pip install -r requirements.txt


Flask uygulamasını çalıştırın:

python app.py


Tarayıcıda http://127.0.0.1:5000
 adresini açın ve bir resim yükleyerek tahmin alın.

Notlar

__pycache__ ve büyük model dosyaları genellikle GitHub’a pushlanmamalıdır

model_c2.h5 → Kullanıcı eğitimi model, eğitim kodu ile birlikte eklenmiştir

converted_savedmodel/ → Google Cloud eğitilmiş model, gerçek tahminlerde kullanılır
