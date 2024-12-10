import tensorflow as tf
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import numpy as np

app = Flask(__name__)


 
# model load and integreating feature
model = tf.keras.models.load_model('model.h5')
class_names = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']
BATCH_SIZE = 32
IMAGE_SIZE = 255
CHANNEL = 3
EPOCHS = 20


# Function to preprocess and predict
def predict(img):
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    return predicted_class, confidence

# home page routing
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', message='No file part')

        file = request.files['file']  # Corrected line

        # If the user does not select a file, browser submits an empty file without a filename
        if file.filename == '':
            return render_template('index.html', message='No selected file')

        # If the file is allowed and has an allowed extension
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join('static', filename)
            file.save(filepath)

            # image reading update
            img = tf.keras.preprocessing.image.load_img(filepath, target_size=(IMAGE_SIZE, IMAGE_SIZE))

            # Predict using the loaded model
            predicted_class, confidence = predict(img)

            # Render the template with the uploaded image, actual and predicted labels, and confidence
            return render_template('index.html', image_path=filepath, actual_label=predicted_class, predicted_label=predicted_class, confidence=confidence)

    return render_template('index.html', message='Upload an image')

# Function to check if the file has an allowed 

