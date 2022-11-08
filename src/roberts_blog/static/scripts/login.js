let login_button = document.getElementById("user-submit");

login_button.addEventListener('mouseover', loginButtonAnimation);
login_button.addEventListener('mouseout', loginButtonAnimationReset);

function loginButtonAnimation() {
    login_button.style.transform = "scale(1.3)";
    login_button.style.transition = "transform 250ms";
}

function loginButtonAnimationReset() {
    login_button.style.transform = 'none';
}

