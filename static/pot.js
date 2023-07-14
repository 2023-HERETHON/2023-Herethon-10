function updateTime() {
    var date = new Date();
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var timeString = hours.toString().padStart(2, '0') + ':' + minutes.toString().padStart(2, '0');
    document.getElementById('time').textContent = timeString;
}

updateTime();
setInterval(updateTime, 1000);

window.onload = function() {
    var selectedImagesData = JSON.parse(localStorage.getItem("selectedImagesData"));
    if (selectedImagesData && selectedImagesData.length > 0) {
        for (var i = 0; i < selectedImagesData.length; i++) {
            var selectedImageSrc = selectedImagesData[i];
            createSelectedImage(selectedImageSrc);
        }
    }
}

function createSelectedImage(imageSrc) {
    var selectedImage = document.createElement("img");
    selectedImage.src = imageSrc;
    selectedImage.alt = "Selected Image";
    selectedImage.style.width = "50px";
    selectedImage.style.height = "50px";
    selectedImage.style.position = "absolute";
    selectedImage.style.left = getRandomPosition(window.innerWidth) + "px";
    selectedImage.style.top = getRandomPosition(window.innerHeight) + "px";
    document.body.appendChild(selectedImage);
}

function getRandomPosition(max) {
    return Math.floor(Math.random() * max);
}

function addSelectedImage() {
    var selectedImageSrc = localStorage.getItem("selectedImageSrc");
    if (selectedImageSrc) {
        createSelectedImage(selectedImageSrc);
        
        var selectedImagesData = JSON.parse(localStorage.getItem("selectedImagesData")) || [];
        selectedImagesData.push(selectedImageSrc);
        localStorage.setItem("selectedImagesData", JSON.stringify(selectedImagesData));
    }
}

function clearSelectedImages() {
    localStorage.removeItem("selectedImagesData");
    var selectedImages = document.querySelectorAll("img[alt='Selected Image']");
    selectedImages.forEach(function(image) {
        image.remove();
    });
}