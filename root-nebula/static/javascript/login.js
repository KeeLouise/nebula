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