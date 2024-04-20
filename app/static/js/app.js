const imageElement = document.getElementById('image');
const ratingInput = document.getElementById('rating');
const ratingSlider = document.getElementById('ratingSlider');
const sliderValue = document.getElementById('sliderValue');

document.addEventListener('DOMContentLoaded', () => {
    const infoBlurb = document.getElementById('infoBlurb');

    // Show the info blurb when the page loads
    infoBlurb.style.display = 'block';

    // Add event listener to hide the info blurb when clicked
    infoBlurb.addEventListener('click', () => {
        infoBlurb.style.display = 'none'; // Hide the info blurb
    });
});


// Update slider value display on input change
ratingSlider.addEventListener('input', () => {
    const currentValue = ratingSlider.value;
    sliderValue.textContent = currentValue;
    updateSliderValuePosition(); // Update position of slider value above the thumb
});

// Handle key press event on the rating input
ratingSlider.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        submitRating(); // Submit rating when Enter key is pressed
    }
});

// Function to update position of slider value above the thumb
function updateSliderValuePosition() {
    const sliderWidth = ratingSlider.offsetWidth;
    const sliderMin = parseFloat(ratingSlider.min);
    const sliderMax = parseFloat(ratingSlider.max);
    const sliderValuePercent = (ratingSlider.value - sliderMin) / (sliderMax - sliderMin);

    const thumbWidth = 20; // Width of the slider thumb
    const thumbPosition = sliderWidth * sliderValuePercent;
    const thumbOffset = thumbPosition - thumbWidth / 2;

    // Calculate left offset relative to the slider container
    const sliderContainerOffsetLeft = ratingSlider.getBoundingClientRect().left;
    const sliderValueOffsetLeft = thumbOffset + sliderContainerOffsetLeft - 263;

    sliderValue.style.left = `${sliderValueOffsetLeft}px`;
}

// Initialize slider value position
updateSliderValuePosition();

function submitRating() {
    const rating = ratingSlider.value;
    const photoId = imageElement.dataset.photoId; // Get the photo ID from data attribute
    console.log(`User rated image ${photoId} as ${rating} cool.`);

    // Send rating data to backend
    saveRatingToBackend(photoId, rating)
        .then(response => {
            console.log(response.message);
            loadNextImage(); // Load the next image after saving the rating
        })
        .catch(error => {
            console.error('Error saving rating:', error);
        });
}

function saveRatingToBackend(photoId, rating) {
    const data = { 'photo_id': photoId, 'rating': rating };

    return fetch('/save_rating', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json());
}

function loadNextImage() {
    const nextImageIndex = Math.floor(Math.random() * 593) + 1; // Assuming you have 16 images
    const imageUrl = `static/images/image${nextImageIndex}.jpg`;

    const maxWidth = 800; // Maximum width for resized image
    const maxHeight = 600; // Maximum height for resized image

    const img = new Image();
    img.onload = function() {
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');

        let width = img.width;
        let height = img.height;

        // Check if image needs resizing
        if (width > maxWidth || height > maxHeight) {
            // Calculate new dimensions while preserving aspect ratio
            if (width > maxWidth) {
                height *= maxWidth / width;
                width = maxWidth;
            }
            if (height > maxHeight) {
                width *= maxHeight / height;
                height = maxHeight;
            }
        }

        // Set canvas dimensions
        canvas.width = width;
        canvas.height = height;

        // Draw image on canvas with resized dimensions
        ctx.drawImage(img, 0, 0, width, height);

        // Convert canvas back to data URL and set as image src
        const resizedImageUrl = canvas.toDataURL('image/jpeg'); // Use 'image/png' for PNG format
        imageElement.src = resizedImageUrl;
        imageElement.dataset.photoId = nextImageIndex; // Update data attribute with new photo ID
        ratingInput.value = '5'; // Reset rating input
    };

    // Load image from URL
    img.src = imageUrl;
}


// Initial load of the first image
loadNextImage();
