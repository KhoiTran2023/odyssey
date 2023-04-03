const loginForm = document.getElementById('login-form');
const loginStatus = document.querySelector('#login-status');
const blurBack = document.getElementById("blur-back");

function toggleLogin() {
    loginForm.style.display = "block";
    blurBack.style.display = "block";
}

function toggleLoginOff() {
    loginForm.style.display = "none";
    blurBack.style.display = " none";
}
const profileURL = "";
fetch('/fetch_url/')
        .then(response => response.json())
        .then(data => {
            profileURL = data.url1;
            console.log(profileURL);
        });

//need to submit convert to function instead of addEventListener
function  submitLogin() {

    const formData = new FormData(loginForm);

    fetch('/log-in/', {
    method: 'POST',
    body: formData
    })
    .then(response => {
    if (response.status === 200) {
        loginStatus.style.display = "inline-block";
        loginStatus.classList.add("alert-success");
        loginStatus.innerHTML = 'You are logged in. Redirecting...';
        setTimeout(() => {window.location.href = profileURL; }, 2000);
        //change this to redirect to profile center
    } else {
        loginStatus.style.display = "inline-block";
        loginStatus.classList.add("alert-info");
        loginStatus.innerHTML = 'Incorrect username or password.';
    }
    })
    .catch(error => {
    console.error(error);
    });
};