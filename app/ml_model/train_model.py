import numpy as np
from preprocess_data import preprocess_image
from retrieve_data import retrieve_data

print("Retrieving data")
data = retrieve_data("ratings")
print("Data Retrieved")
num_images = len(data)

# Preprocess the data
X = []  # Features (image data or extracted features)
y = []  # Target (ratings)

print("Beginning image processing")
for i, image_number, rating in data:
    print(f"processing image: {i}/{num_images}")
    # Load and preprocess image corresponding to image_number (you can use OpenCV or other libraries)
    img_features = preprocess_image(image_number)  # Function to extract image features
    X.append(img_features)
    y.append(rating)

X = np.array(X)
y = np.array(y)

print("import tensorflow packages")
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
print("done importing")

print("defining simple NN")
# Define a simple neural network model
model = Sequential([
    Dense(128, activation='relu', input_shape=(X.shape[1],)),  # Input layer
    Dense(64, activation='relu'),  # Hidden layer
    Dense(1)  # Output layer (single neuron for regression)
])
print("done with simple NN")

print("compiling model")
# Compile the model
model.compile(optimizer='adam', loss='mse')  # Mean squared error loss for regression

print("training model")
# Train the model
model.fit(X, y, epochs=10, batch_size=32, validation_split=0.2)

from sklearn.model_selection import train_test_split

print("training test split")
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.ensemble import GradientBoostingRegressor

model = GradientBoostingRegressor()

print("fitting model to GradentBoostingRegressor")
model.fit(X_train, y_train)

from sklearn.metrics import mean_squared_error, r2_score

y_pred = model.predict(X_val)
mse = mean_squared_error(y_val, y_pred)
r2 = r2_score(y_val, y_pred)
print(f"Validation MSE: {mse}, R^2 Score: {r2}")

import joblib

joblib.dump(model, 'coolness_model.pkl')
