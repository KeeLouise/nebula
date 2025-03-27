document.getElementById("createAccount").addEventListener("submit", function(event) {
    // This will clear any previous error messages - KR 26/03/2025
    const emailError = document.getElementById("emailError");
    const passwordError = document.getElementById("passwordError");
    const confirmPasswordError = document.getElementById("confirmPasswordError");
    emailError.textContent = "";
    passwordError.textContent = "";
    confirmPasswordError.textContent = "";

    // This will retrieve form values - KR 26/03/2025
    var fullName = document.getElementById("fullname").value;
    var email = document.getElementById("inputEmail1").value;
    var password = document.getElementById("inputPassword1").value;
    var confirmPassword = document.getElementById("inputPassword2").value;

    var valid = true;

    // The below is to validate the Full Name field - KR 26/03/2025
    if (fullName.trim() === "") {
        alert("Please provide your full name.");
        valid = false;
    }

    //Email validation - copied from login.js - KR 26/03/2025
    if (!emailRegex.test(email)) {
        event.preventDefault();  // Prevent form submission - KR 26/03/2025
        emailError.textContent = "Please enter a valid email address.";
        emailError.style.color = "red";
    }

    // Password validation - KR 26/03/2025
    if (password.length < 8){
        passwordError.textContent = "Password must be at least 8 characters long.";
        passwordError.style.color = "red";
        valid = false;
    }

    // This is further validation for confirm password - KR 26/03/2025
    if(password !== confirmPassword){
        confirmPasswordError.textContent = "Passwords do not match. Please re-enter your password.";
        confirmPasswordError.style.color = "red";
        valid = false;
    }

    // If any of the above validation fails, prevent form submission - KR 26/03/2025
    if (!valid) {
        event.preventDefault();
    }
});

