// Auto-dismiss flash message after 3 seconds – KR 16/04/2025
document.addEventListener("DOMContentLoaded", function () {
    const flash = document.getElementById("flash-message");
    if (flash) {
      setTimeout(() => {
        flash.classList.remove("show"); // Bootstrap class – KR 16/04/2025
        flash.classList.add("fade");    // Bootstrap class – KR 16/04/2025
        flash.style.transition = "opacity 0.5s ease-out"; // Smooth fade – KR 16/04/2025
        flash.style.opacity = 0;
  
        // Optional: remove from DOM after fade – KR 16/04/2025
        setTimeout(() => flash.remove(), 500);
      }, 3000); // Flash disappears after 3 seconds – KR 16/04/2025
    }
  
    // Form validation logic – KR 26/03/2025
    const form = document.getElementById("createAccount");
    if (!form) return;
  
    form.addEventListener("submit", function (event) {
      // Define regex for email validation – KR 13/04/2025
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  
      // This will clear any previous error messages – KR 26/03/2025
      const emailError = document.getElementById("emailError");
      const passwordError = document.getElementById("passwordError");
      const confirmPasswordError = document.getElementById("confirmPasswordError");
  
      emailError.textContent = "";
      passwordError.textContent = "";
      confirmPasswordError.textContent = "";
  
      // Retrieve form values – KR 26/03/2025
      const fullName = document.getElementById("fullname").value;
      const email = document.getElementById("inputEmail1").value;
      const password = document.getElementById("inputPassword1").value;
      const confirmPassword = document.getElementById("inputPassword2").value;
  
      let valid = true;
  
      // Validate the Full Name field – KR 26/03/2025
      if (fullName.trim() === "") {
        alert("Please provide your full name.");
        valid = false;
      }
  
      // Email validation – KR 26/03/2025
      if (!emailRegex.test(email)) {
        emailError.textContent = "Please enter a valid email address.";
        emailError.style.color = "red";
        valid = false;
      }
  
      // Password validation – KR 26/03/2025
      if (password.length < 8) {
        passwordError.textContent = "Password must be at least 8 characters long.";
        passwordError.style.color = "red";
        valid = false;
      }
  
      // Confirm Password validation – KR 26/03/2025
      if (password !== confirmPassword) {
        confirmPasswordError.textContent = "Passwords do not match. Please re-enter your password.";
        confirmPasswordError.style.color = "red";
        valid = false;
      }
  
      // If any validation fails, prevent submission – KR 26/03/2025
      if (!valid) {
        event.preventDefault();
      }
    });
  });
