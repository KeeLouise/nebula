document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("loginForm").addEventListener("submit", function(event) {
        var email = document.getElementById("exampleInputEmail1").value;
        var emailError = document.getElementById("emailError");
        var emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;

        // This will clear any previous error messages - KR 26/03/2025
        emailError.textContent = "";

        // use of regular expressions to check the email format - KR 26/03/2025
        if (!emailRegex.test(email)) {
            event.preventDefault();  // Prevent form submission - KR 26/03/2025
            emailError.textContent = "Please enter a valid email address.";
            emailError.style.color = "red";
        }
    });
});