document.addEventListener("DOMContentLoaded", function () {
    const hamburger = document.querySelector(".hamburger-menu");
    const mobileNav = document.querySelector("#mobile-nav");

    hamburger.addEventListener("click", function () {
        mobileNav.classList.toggle("active");
    });

    const commentButtons = document.querySelectorAll(".toggle-comment");

    commentButtons.forEach(button => {
        button.addEventListener("click", function () {
            const formId = this.getAttribute("data-target");
            const form = document.getElementById(formId);

            if (form.style.display === "none" || form.style.display === "") {
                form.style.display = "block";
                this.textContent = "Hide Comment";
            } else {
                form.style.display = "none";
                this.textContent = "Comment";
            }
        });
    });

    const toggle = document.getElementById('guidelines-toggle');
    const content = document.getElementById('guidelines-content');
    
    toggle.addEventListener('click', () => {
        content.classList.toggle('show');
    });
});
