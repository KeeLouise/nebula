function validateEmail(email) {
// Regular expression to check email format
   const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
   return emailPattern.test(email);
}
function validateForm() {
    const email = document.getElementById("email").value;
        if (!validateEmail(email)) {
            alert("Please enter a valid email address.");
            return false;
            }
            return true;
}

function validatePassword(password) {
    const minLength = 8;
    const hasUpperCase = /[A-Z]/.test(password);
    const hasLowerCase = /[a-z]/.test(password);
    const hasNumber = /\d/.test(password);
    const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(password);

    // Check if all conditions are met by user
    if (password.length >= minLength && hasUpperCase && hasLowerCase && hasNumber && hasSpecialChar) {
        return true;
    } else {
        return false;
    }
}