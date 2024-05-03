import joblib
import numpy as np
from preprocess_data import *
import os
from retrieve_data import retrieve_data
import pandas as pd
import matplotlib.pyplot as plt

data = retrieve_data("ratings")

ratings = {}


for i, image_number, rating in data:
    if image_number in ratings:
        ratings[image_number] = np.append(ratings[image_number], rating)
    else:
        ratings[image_number] = np.array([rating])


for image in ratings:
    ratings[image] = np.average(ratings[image])

print(ratings)

# Initialize lists to collect data
filenames = []
img_numbers = []
predicted_scores = []
user_ratings = []

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
    # Extract features from the image
    color_features = extract_color_histogram(image)
    texture_features = extract_texture_features(image)
    shape_features = extract_shape_features(image)
    # Concatenate features into a single array
    features = np.concatenate([color_features, texture_features, shape_features])
    return features

# Path to the folder containing image files
folder_path = '../static/images'

# Iterate over each image file in the folder
i = 1
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Construct the full path to the image file
        image_path = os.path.join(folder_path, filename)
        print(image_path)

        img_num = int(''.join(char for char in filename if char.isdigit()))

        # Preprocess the image
        features = preprocess_new_image(image_path)

        # Reshape features array to match the input shape expected by the model
        features = np.array([features])

        # Make prediction using the model
        predicted_coolness_score = model.predict(features)

        # Print the predicted coolness score for the current image
        print(f"Image: {filename}, Predicted Coolness Score: {predicted_coolness_score[0]}")
        if img_num in list(ratings.keys()):
            print(f"User rating of image: {img_num}: {ratings[img_num]}")
        else:
            print("No user ratings for this photo")
        print(f"iteration: {i}/594?")
        i+=1
        # Collect data for DataFrame
        filenames.append(filename)
        img_numbers.append(img_num)
        predicted_scores.append(predicted_coolness_score[0])
        user_ratings.append(ratings.get(img_num, np.nan))  # Get user rating or NaN if not available

# Create a Pandas DataFrame
data = {
    'Filename': filenames,
    'Image_Number': img_numbers,
    'Predicted_Coolness_Score': predicted_scores,
    'User_Rating': user_ratings
}

df = pd.DataFrame(data)
sorted_df = df.sort_values(by='Image_Number', ascending=True)
max_rating = df.loc[df['Predicted_Coolness_Score'].idxmax()]
top_5_by_column = df.sort_values(by='Predicted_Coolness_Score', ascending=False).head(5)
bot = df.sort_values(by='Predicted_Coolness_Score', ascending=True).head(5)

print(top_5_by_column)
print(max_rating)
print(bot)
# Display the DataFrame
print(sorted_df)



plt.figure(figsize=(8, 5))
plt.plot(sorted_df['Image_Number'], sorted_df['User_Rating'] - sorted_df['Predicted_Coolness_Score'], label='User Rating', marker = 'o', linestyle=' ')
# plt.plot(sorted_df['Image_Number'], sorted_df['Predicted_Coolness_Score'], marker='o', linestyle=' ', label='Predicted by Model')
plt.legend()
plt.grid(True)
plt.show()