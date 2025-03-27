document.addEventListener("DOMContentLoaded", function () {
    const hamburger = document.querySelector(".hamburger-menu");
    const mobileNav = document.querySelector("#mobile-nav");

    hamburger.addEventListener("click", function () {
        mobileNav.classList.toggle("active");
    });
});


