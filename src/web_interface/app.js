const imageElement = document.getElementById('image');
const ratingInput = document.getElementById('rating');

function submitRating() {
    const rating = ratingInput.value;
    console.log(`User rated image as ${rating} cool.`);
    // Add logic to send rating data to backend or process it further
    // For now, simply load the next image
    loadNextImage();
}

function loadNextImage() {
    // Simulate loading the next image (replace with actual logic)
    const nextImageIndex = Math.floor(Math.random() * 10) + 1; // Assuming you have 10 images
    imageElement.src = `images/image${nextImageIndex}.jpg`;
    ratingInput.value = '5'; // Reset rating input
}

// Initial load of the first image
loadNextImage();
