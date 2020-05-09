/* When the user clicks on the button, 
        toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}
    
    // Close the dropdown if the user clicks outside of it
    window.onclick = function(e) {
    if (!e.target.matches('.dropbtn')) {
    var myDropdown = document.getElementById("myDropdown");
        if (myDropdown.classList.contains('show')) {
        myDropdown.classList.remove('show');
        }
    }
}

// Image Slider
const slides = document.querySelectorAll('.slide');
const next = document.querySelector('#next');
const prev = document.querySelector('#prev');
const auto = false;
const intervalTime = 5000;
let slideInterval;

const nextSlide = () => {
    // Get Current Class
    const current = document.querySelector('.current');
    // Remove Current Class
    current.classList.remove('.current');
    // Check for next slide
    if(current.nextElementSibling){
        // Add current to next sibiling
        current.nextElementSibling.classList.add('current');
    } else {
        // Add current to start
        slides[0].classList.add('current');
    }
    setTimeout(() => current.classList.remove('current'))
}

const prevSlide = () => {
    // Get Current Class
    const current = document.querySelector('.current');
    // Remove Current Class
    current.classList.remove('.current');
    // Check for prev slide
    if(current.previousElementSibling){
        // Add current to prev sibiling
        current.previousElementSibling.classList.add('current');
    } else {
        // Add current to last
        slides[slides.length - 1].classList.add('current');
    }
    setTimeout(() => current.classList.remove('current'))
}

// Button events
next.addEventListener('click', e => {
    nextSlide();
    if(auto) {
        clearInterval();
        slideInterval = setInterval(nextSlide, intervalTime);
    }
});

prev.addEventListener('click', e => {
    prevSlide();
    if(auto) {
        clearInterval();
        slideInterval = setInterval(nextSlide, intervalTime);
    }
});

// Auto slide
if(auto) {
    // Run next slide at interval time
    slideInterval = setInterval(nextSlide, intervalTime)
}