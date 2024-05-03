# coolness_factor
### Project README

#### Project Data Structure

This project implements a simple machine learning pipeline for analyzing image data. The main components of the project include:

1. **preprocess_data.py**: This module contains functions for preprocessing image data. It includes functions for extracting color histograms, texture features using Gray-Level Co-occurrence Matrices (GLCM), and shape-based features such as contour area and perimeter.

2. **train_model.py**: This script trains a machine learning model using the preprocessed image data. It uses features extracted from images to predict a "coolness" score. The model architecture includes a simple neural network and optionally a Gradient Boosting Regressor.

3. **test_model.py**: This script tests the trained model on new images. It preprocesses new images and uses the trained model to predict the coolness score of each image.

4. **test_against_data.py**: This script compares the predictions made by the trained model against user ratings stored in a database. It preprocesses images, predicts coolness scores, and compares them with user ratings to evaluate model performance.

5. **retrieve_data.py**: This module provides functions to retrieve data from a SQLite database. It connects to the database, executes SQL queries to retrieve data, and returns the results.

#### Explanation of the Data Structure

The data structure of this project involves a pipeline for processing and analyzing image data. It consists of the following steps:

1. **Data Retrieval**: Image data and corresponding user ratings are retrieved from a SQLite database using SQL queries.

2. **Data Preprocessing**: Image data is preprocessed using techniques such as resizing, histogram computation, texture feature extraction, and shape-based feature extraction.

3. **Model Training**: A machine learning model is trained using the preprocessed image data. The model learns to predict a "coolness" score based on extracted features.

4. **Model Testing**: The trained model is tested on new images to predict their coolness scores. These predictions are compared against user ratings to evaluate model performance.

#### Running the Project

To run the project, follow these steps:

1. Ensure you have Python installed on your system (version 3.6 or higher recommended).

2. Install the required dependencies by running the following command in your terminal:

   ```bash
   pip install -r requirements.txt
   ```

3. Prepare your image data and store user ratings in a SQLite database.

4. Modify the database path and SQL queries in `retrieve_data.py` to match your database setup.

5. Run the scripts in the following order:

   - `train_model.py`: Train the machine learning model using preprocessed image data.
   - `test_model.py`: Test the trained model on new images to predict their coolness scores.
   - `test_against_data.py`: Compare model predictions against user ratings stored in the database to evaluate model performance.

6. Follow the instructions provided by each script to input necessary parameters or paths.

Note: Make sure your image data is organized and named correctly according to the expected file paths in the scripts.

#### Data Collection

#### Data Collection

The data for this project was collected using a website created with Flask, which was hosted locally on a Mac. The website was accessible at coolness-factor.duckdns.org and was promoted through various channels including a class Piazza, Reddit, and among friends and family. 

The website randomly presented users with images from the `/app/static/images` folder, comprising a total of 593 images sourced online. For each image, users were prompted to rate its "coolness" on a scale from 0 to 10 using a slider. 

Throughout the collection period, approximately 900 ratings were obtained. However, many images remained unrated, and most received only one rating. This limited data affects the model's learning process, resulting in a tendency for the model to closely mimic user ratings, with some exceptions where deviations occur.

The impact of this data limitation can be observed in the comparison between the model's ratings and those provided by users. This comparison is explored in the `test_against_data.py` script. Additionally, the script outputs the lowest and highest rated images, allowing users to check if they agree with the ratings. 

While the model's ratings for the "coolest" images were generally in agreement with user ratings, there was some controversy regarding the "uncoolest" images. 

A plot depicting the difference between user and model ratings is also generated. Large spikes in the plot are likely due to images that were not rated by users, resulting in outliers where the model's opinion significantly differs from the user's. This discrepancy can be attributed to the low sample size and the absence of user ratings for certain images.

Below are screenshots of the website for reference, in case it is taken down before evaluation.


![alt text](image.png)

![alt text](image-1.png)