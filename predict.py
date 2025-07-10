from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

np.set_printoptions(suppress=True)

model = load_model("keras_model.h5", compile=False)

class_names = open("labels.txt", "r").readlines()

def prepare_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
    image_array = np.asarray(image) / 255.0
    return np.expand_dims(image_array, axis=0)

image_files = ["test.jpg", "test1.jpg"]

for image_file in image_files:
    image = prepare_image(image_file)
    prediction = model.predict(image)
    predicted_index = np.argmax(prediction)
    predicted_label = class_names[predicted_index].strip()

    print(f"{image_file} → Predicted class: {predicted_label}")
