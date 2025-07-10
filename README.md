# 🧠 Image Classifier using Teachable Machine

This project is an image classification model built using **Teachable Machine by Google**, exported in **TensorFlow Keras format**, and used in a Python script to classify images.

## 📌 Task Description

- Train an image classifier with at least two classes using Teachable Machine.
- Export the trained model as **Keras (.h5)** format.
- Load and use the model in a Python script to classify images.
- Test using at least 2 different images and print predicted classes.
- Submit the script, model files, and screenshot of results on GitHub.

## 📁 Files in this repo

| File            | Description                          |
|-----------------|--------------------------------------|
| `keras_model.h5` | Trained Keras model file             |
| `labels.txt`     | List of class labels (e.g., snake, crocodile) |
| `predict.py`     | Python script to classify images     |
| `test.jpg`       | Image of a **crocodile**             |
| `test1.jpg`      | Image of a **snake**                 |
| `README.md`      | This file                            |

## 🧪 How to Run

1. Install dependencies:

```bash
pip install tensorflow keras pillow numpy

Run the script:

python predict.py

You should see output like:

test.jpg  => Predicted class: crocodile
test1.jpg => Predicted class: snake
```
## 📸 Screenshot

![Output](./output.png)

## 🛠 Made by: Musaad Al-Ghashmari
