import io
from flask import Flask, render_template, request, Response
from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

model = load_model("./model_c2.h5")
print(model.input_shape)

dataset = tf.keras.preprocessing.image_dataset_from_directory(
    'dataset_train',  # Directory with subfolders representing class labels
    image_size=(300, 300),  # Resize images (match with what your model expects)
    batch_size=32  # Adjust as needed
)

@app.route('/', methods=["GET", "POST"])
def home() -> Response:
    if request.method == "GET":
        return render_template('index2.html')
    
    uploaded_file: bytes = request.files["file"].read()
    image = Image.open(io.BytesIO(uploaded_file)).resize((224, 224))
    img_array = np.array(image)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=-1)[0]
    # return render_template("akdaslkda.html")
    class_names = dataset.class_names
    return class_names[predicted_class]


if __name__ == '__main__':
    app.run(debug=True)