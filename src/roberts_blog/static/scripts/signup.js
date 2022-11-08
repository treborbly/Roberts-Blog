let signup_button = document.getElementById('user-submit');

signup_button.addEventListener('mouseover', signupButtonAnimation);
signup_button.addEventListener('mouseout', signupButtonAnimationReset);

function signupButtonAnimation() {
    signup_button.style.transform = "scale(1.3)";
    signup_button.style.transition = "transform 250ms";
}

function signupButtonAnimationReset() {
    signup_button.style.transform = 'none';
}