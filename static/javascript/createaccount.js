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
    var email = document.getElementById("exampleInputEmail1").value;
    var password = document.getElementById("exampleInputPassword1").value;
    var confirmPassword = document.getElementById("exampleInputPassword2").value;

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
