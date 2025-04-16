document.addEventListener("DOMContentLoaded", function () {
    // Flash message dismiss – KR 16/04/2025
    const flash = document.getElementById("flash-message");
    if (flash) {
      setTimeout(() => {
        flash.classList.remove("show");
        flash.classList.add("fade");
        flash.style.transition = "opacity 0.5s ease-out";
        flash.style.opacity = 0;
        setTimeout(() => flash.remove(), 500);
      }, 3000);
    }
  
    // Mobile menu toggle – KR 26/03/2025
    const hamburger = document.querySelector(".hamburger-menu");
    const mobileNav = document.querySelector("#mobile-nav");
  
    if (hamburger && mobileNav) {
      hamburger.addEventListener("click", function () {
        mobileNav.classList.toggle("active");
      });
    }
  
    // Toggle comment form – KR 26/03/2025
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
  
    // Collapsible comments toggle – KR 16/04/2025
    document.querySelectorAll('.toggle-comments').forEach(button => {
      button.addEventListener('click', () => {
        const targetId = button.getAttribute('data-target');
        const commentsEl = document.getElementById(targetId);
  
        if (commentsEl.style.display === 'none' || commentsEl.style.display === '') {
          commentsEl.style.display = 'block';
          button.textContent = 'Hide Comments';
        } else {
          commentsEl.style.display = 'none';
          const count = commentsEl.querySelectorAll('li').length;
          button.textContent = `Show Comments (${count})`;
        }
      });
    });
  
    // Like button toggle – KR 16/04/2025
    document.querySelectorAll('.like-btn').forEach(button => {
      button.addEventListener('click', () => {
        const postId = button.getAttribute('data-post-id');
  
        fetch(`/toggle_like/${postId}`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
          }
        })
          .then(res => res.json())
          .then(data => {
            if (data.likes !== undefined) {
              const countSpan = document.getElementById(`like-count-${postId}`);
              countSpan.textContent = data.likes;
  
              const icon = button.querySelector('i');
  
              if (button.classList.contains('btn-outline-primary')) {
                button.classList.remove('btn-outline-primary');
                button.classList.add('btn-primary');
                icon.classList.remove('bi-rocket');
                icon.classList.add('bi-rocket-fill');
              } else {
                button.classList.remove('btn-primary');
                button.classList.add('btn-outline-primary');
                icon.classList.remove('bi-rocket-fill');
                icon.classList.add('bi-rocket');
              }
            }
          });
      });
    });

    // Post search filter – KR 16/04/2025
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
    
    // Community Guidelines toggle – KR 16/04/2025
    const guidelinesToggle = document.getElementById("guidelines-toggle");
    const guidelinesContent = document.getElementById("guidelines-content");
    
    if (guidelinesToggle && guidelinesContent) {
      guidelinesToggle.addEventListener("click", () => {
        guidelinesContent.classList.toggle("show");
      });
    }
  });