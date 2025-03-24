document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const email = document.getElementById("exampleInputEmail1");
    const password = document.getElementById("exampleInputPassword1");
    const confirmPassword = document.getElementById("exampleInputPassword2");

    form.addEventListener("submit", function (event) {
        if (!validateForm()) {
            event.preventDefault(); // Prevent form submission if validation fails
        }
    });

    function validateForm() {
        if (!validateEmail(email.value)) {
            alert("Please enter a valid email address.");
            email.classList.add("is-invalid");
            return false;
        } else {
            email.classList.remove("is-invalid");
        }

        if (!validatePassword(password.value)) {
            alert("Password must be at least 8 characters long and include an uppercase letter, a lowercase letter, a number, and a special character.");
            password.classList.add("is-invalid");
            return false;
        } else {
            password.classList.remove("is-invalid");
        }

        if (!validatePasswordMatch()) {
            alert("Passwords do not match. Please try again.");
            confirmPassword.classList.add("is-invalid");
            return false;
        } else {
            confirmPassword.classList.remove("is-invalid");
        }

        return true;
    }

    function validateEmail(email) {
        const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        return emailPattern.test(email);
    }

    function validatePassword(password) {
        const minLength = 8;
        const hasUpperCase = /[A-Z]/.test(password);
        const hasLowerCase = /[a-z]/.test(password);
        const hasNumber = /\d/.test(password);
        const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(password);

        return password.length >= minLength && hasUpperCase && hasLowerCase && hasNumber && hasSpecialChar;
    }

    function validatePasswordMatch() {
        return password.value === confirmPassword.value;
    }

    // realtime validation for password match
    confirmPassword.addEventListener("input", function () {
        if (password.value !== confirmPassword.value) {
            confirmPassword.classList.add("is-invalid");
        } else {
            confirmPassword.classList.remove("is-invalid");
        }
    });

    // realtime validation for email
    email.addEventListener("input", function () {
        if (validateEmail(email.value)) {
            email.classList.remove("is-invalid");
        } else {
            email.classList.add("is-invalid");
        }
    });

    // realtime validation for password strength
    password.addEventListener("input", function () {
        if (validatePassword(password.value)) {
            password.classList.remove("is-invalid");
        } else {
            password.classList.add("is-invalid");
        }
    });
});