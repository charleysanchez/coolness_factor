import numpy as np
import cv2
from skimage.feature import graycomatrix, graycoprops


def preprocess_image(image_id):
    image_filename = f'../static/images/image{image_id}.jpg'
    image = cv2.imread(image_filename)

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


def extract_color_histogram(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Compute color histograms for each channel (R, G, B)
    hist_r = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([image], [1], None, [256], [0, 256])
    hist_b = cv2.calcHist([image], [2], None, [256], [0, 256])

    # Normalize histograms (optional but often recommended)
    hist_r = cv2.normalize(hist_r, hist_r).flatten()
    hist_g = cv2.normalize(hist_g, hist_g).flatten()
    hist_b = cv2.normalize(hist_b, hist_b).flatten()

    # Concatenate histograms into a single feature vector
    color_features = np.concatenate((hist_r, hist_g, hist_b))

    return color_features


def extract_texture_features(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    distances = [1, 2, 3]
    angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]
    glcm = graycomatrix(image, distances=distances, angles=angles, symmetric=True, normed=True)

    contrast = graycoprops(glcm, 'contrast')
    energy = graycoprops(glcm, 'energy')
    correlation = graycoprops(glcm, 'correlation')
    homogeneity = graycoprops(glcm, 'homogeneity')

    texture_features = np.concatenate([contrast.ravel(), energy.ravel(), correlation.ravel(), homogeneity.ravel()])

    return texture_features


def extract_shape_features(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Thresholding and contour extraction
    _, thresh = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Extract shape-based features (e.g., contour area, perimeter)
    shape_features = []
    for contour in contours:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, closed=True)
        shape_features.append(area)
        shape_features.append(perimeter)

    shape_features = np.array(shape_features)
    shape_features = pad_or_trim_features(shape_features, desired_length=500)


    return shape_features


def pad_or_trim_features(features, desired_length):
    current_length = len(features)
    
    if current_length < desired_length:
        # Pad features with zeros to match desired length
        padded_features = np.pad(features, (0, desired_length - current_length), mode='constant')
    elif current_length > desired_length:
        # Truncate features to match desired length
        padded_features = features[:desired_length]
    else:
        padded_features = features
    
    return padded_features