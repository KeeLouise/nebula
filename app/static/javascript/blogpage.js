document.addEventListener("DOMContentLoaded", function () {
    const flash = document.getElementById("flash-message");
    if (flash) {
      setTimeout(() => {
        flash.classList.remove("show");  // Bootstrap class - KR 16/04/2025
        flash.classList.add("fade");     // Bootstrap class - KR 16/04/2025
        flash.style.transition = "opacity 0.5s ease-out";
        flash.style.opacity = 0;

        // remove from DOM after fade – KR 16/04/2025
        setTimeout(() => flash.remove(), 500);
      }, 3000); // Flash disappears after 3 seconds – KR 16/04/2025
    }


    const hamburger = document.querySelector(".hamburger-menu");
    const mobileNav = document.querySelector("#mobile-nav");

    if (hamburger && mobileNav) {
        hamburger.addEventListener("click", function () {
            mobileNav.classList.toggle("active");
        });
    }

    const commentButtons = document.querySelectorAll(".toggle-comment");

    commentButtons.forEach(button => {
        button.addEventListener("click", function () {
            const formId = this.getAttribute("data-target");
            const form = document.getElementById(formId);

            if (form.style.display === "none" || form.style.display === "") {
                form.style.display = "block";
                this.textContent = "Comment";
            } else {
                form.style.display = "none";
                this.textContent = "Comment";
            }
        });
    });

    const toggle = document.getElementById("guidelines-toggle");
    const content = document.getElementById("guidelines-content");

    if (toggle && content) {
        toggle.addEventListener("click", function () {
            content.classList.toggle("show");
        });
    }

    const searchInput = document.getElementById("post-search");
    const posts = document.querySelectorAll(".post-scroll .card");

    if (searchInput && posts.length > 0) {
        searchInput.addEventListener("input", function () {
            const query = this.value.toLowerCase();
            posts.forEach(post => {
                const text = post.textContent.toLowerCase();
                post.style.display = text.includes(query) ? "block" : "none";
            });
        });
    }
});
