document.addEventListener("DOMContentLoaded", function () {
    // Auto dismiss flash messages– KR 16/04/2025
    const flash = document.getElementById("flash-message");
    if (flash) {
      setTimeout(() => {
        flash.classList.remove("show");  // Bootstrap class - KR 16/04/2025
        flash.classList.add("fade");     // Bootstrap class - KR 16/04/2025
        flash.style.transition = "opacity 0.5s ease-out";
        flash.style.opacity = 0;
        flash.style.scale = 

        // remove from DOM after fade – KR 16/04/2025
        setTimeout(() => flash.remove(), 500);
      }, 3000); // Flash disappears after 3 seconds – KR 16/04/2025
    }

    // LOGIN FORM EMAIL VALIDATION – KR 26/03/2025
    const loginForm = document.getElementById("loginForm");
    if (!loginForm) return;

    loginForm.addEventListener("submit", function (event) {
      // Retrieve email input and error display element – KR 26/03/2025
      const emailInput = document.getElementById("email");
      const emailError = document.getElementById("emailError");

      // Regular expression for email validation – KR 26/03/2025
      const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;

      // This will clear any previous error messages – KR 26/03/2025
      emailError.textContent = "";

      // Use of regular expressions to check the email format – KR 26/03/2025
      if (!emailRegex.test(emailInput.value)) {
        event.preventDefault();  // Prevent form submission – KR 26/03/2025
        emailError.textContent = "Please enter a valid email address.";
        emailError.style.color = "red";
      }
    });
  });