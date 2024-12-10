from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

app = Flask(__name__)
model = load_model('models/potato_disease_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    image = Image.open(file).resize((128, 128))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    prediction = model.predict(image_array)
    label = 'Healthy' if np.argmax(prediction) == 0 else 'Diseased'
    return jsonify({'prediction': label})

if __name__ == '__main__':
    app.run(debug=True)
