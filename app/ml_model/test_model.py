import joblib
import numpy as np
from preprocess_data import *
import os


# Load the trained model
model = joblib.load('coolness_model.pkl')

def preprocess_new_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        return None
    
    img_size = (400, 400)
    image_resized = cv2.resize(image, img_size)

    color_features = extract_color_histogram(image_resized)
    print(color_features.shape)

    texture_features = extract_texture_features(image_resized)
    print(texture_features.shape)

    shape_features = extract_shape_features(image_resized)
    print(shape_features.shape)


    features = np.concatenate([color_features, texture_features, shape_features])

    return features

def load_and_preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (400, 400))
    return image

def extract_features(image):
    color_features = extract_color_histogram(image)
    texture_features = extract_texture_features(image)
    shape_features = extract_shape_features(image)
    features = np.concatenate([color_features, texture_features, shape_features])
    return features

# Path to the folder containing image files
folder_path = 'test_images'

# Iterate over each image file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Construct the full path to the image file
        image_path = os.path.join(folder_path, filename)
        print(image_path)

        # Preprocess the image
        features = preprocess_new_image(image_path)

        # Reshape features array to match the input shape expected by the model
        features = np.array([features])

        # Make prediction using the model
        predicted_coolness_score = model.predict(features)

        # Print the predicted coolness score for the current image
        print(f"Image: {filename}, Predicted Coolness Score: {predicted_coolness_score[0]}")

