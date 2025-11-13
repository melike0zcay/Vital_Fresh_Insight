import io
from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2

app = Flask(__name__)

# Model ve etiket dosyalarını yükle
model = tf.keras.layers.TFSMLayer('converted_savedmodel/model.savedmodel', call_endpoint='serving_default')
class_names = open("converted_savedmodel/labels.txt", "r").readlines()

@app.route('/')
def home():
    return render_template('index.html', class_names=[name.strip() for name in class_names])

@app.route('/analyze', methods=["POST"])
def analyze():
    try:
        # Kullanıcıdan gelen dosyayı işle
        uploaded_file = request.files["file"].read()
        image = Image.open(io.BytesIO(uploaded_file)).convert("RGB")
        image = image.resize((224, 224))  # Model giriş boyutuna göre yeniden boyutlandır

        # Resmi numpy dizisine dönüştür ve normalize et
        img_array = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
        img_array = (img_array / 127.5) - 1  # Normalizasyon

        # Model tahmini yap
        predictions = model(img_array)

        # Çıktı anahtarını belirle ve tahminleri al
        output_key = list(predictions.keys())[0]
        predictions = predictions[output_key].numpy()

        # Tahmin edilen sınıfı ve güven skorunu al
        predicted_class_index = np.argmax(predictions)
        predicted_class_name = class_names[predicted_class_index].strip()
        confidence_score = predictions[0][predicted_class_index]

        # Sonuçları JSON formatında döndür
        return jsonify({
            "prediction": predicted_class_name,
            "confidence": f"{confidence_score:.2%}",
            "class_names": [name.strip() for name in class_names]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)