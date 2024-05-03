const imageElement = document.getElementById('image');
const ratingInput = document.getElementById('rating');
const ratingSlider = document.getElementById('ratingSlider');
const sliderValue = document.getElementById('sliderValue');

document.addEventListener('DOMContentLoaded', () => {
    const infoBlurb = document.getElementById('infoBlurb');

    infoBlurb.style.display = 'block';

    infoBlurb.addEventListener('click', () => {
        infoBlurb.style.display = 'none';
    });
});


ratingSlider.addEventListener('input', () => {
    const currentValue = ratingSlider.value;
    sliderValue.textContent = currentValue;
    updateSliderValuePosition();
});

ratingSlider.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        submitRating();
    }
});

function updateSliderValuePosition() {
    const sliderWidth = ratingSlider.offsetWidth;
    const sliderMin = parseFloat(ratingSlider.min);
    const sliderMax = parseFloat(ratingSlider.max);
    const sliderValuePercent = (ratingSlider.value - sliderMin) / (sliderMax - sliderMin);

    const thumbWidth = 20;
    const thumbPosition = sliderWidth * sliderValuePercent;
    const thumbOffset = thumbPosition - thumbWidth / 2;

    const sliderContainerOffsetLeft = ratingSlider.getBoundingClientRect().left;
    const sliderValueOffsetLeft = thumbOffset + sliderContainerOffsetLeft - 263;

    sliderValue.style.left = `${sliderValueOffsetLeft}px`;
}

updateSliderValuePosition();

function submitRating() {
    const rating = ratingSlider.value;
    const photoId = imageElement.dataset.photoId;
    console.log(`User rated image ${photoId} as ${rating} cool.`);

    saveRatingToBackend(photoId, rating)
        .then(response => {
            console.log(response.message);
            loadNextImage();
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
    const nextImageIndex = Math.floor(Math.random() * 593) + 1;
    const imageUrl = `static/images/image${nextImageIndex}.jpg`;

    const maxWidth = 800;
    const maxHeight = 600;

    const img = new Image();
    img.onload = function() {
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');

        let width = img.width;
        let height = img.height;

        if (width > maxWidth || height > maxHeight) {
            if (width > maxWidth) {
                height *= maxWidth / width;
                width = maxWidth;
            }
            if (height > maxHeight) {
                width *= maxHeight / height;
                height = maxHeight;
            }
        }

        canvas.width = width;
        canvas.height = height;

        ctx.drawImage(img, 0, 0, width, height);

        const resizedImageUrl = canvas.toDataURL('image/jpeg');
        imageElement.src = resizedImageUrl;
        imageElement.dataset.photoId = nextImageIndex;
        ratingInput.value = '5';
    };

    img.src = imageUrl;
}


loadNextImage();
