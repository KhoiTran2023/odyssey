const loginForm = document.querySelector('#login-form');
const loginStatus = document.querySelector('#login-status');
var indexUrl = "";

function toggleLogin() {
    loginForm.style.display = "block";
}

function toggleLoginOff() {
    loginForm.style.display = "none";
}

fetch('/fetch_url/')
        .then(response => response.json())
        .then(data => {
            indexUrl = data.url1;
            console.log(indexUrl);
        });

//need to submit convert to function instead of addEventListener
loginForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const formData = new FormData(loginForm);

    fetch('/log-in/', {
    method: 'POST',
    body: formData
    })
    .then(response => {
    if (response.status === 200) {
        loginStatus.style.display = "inline-block";
        loginStatus.classList.add("alert-success");
        loginStatus.innerHTML = 'You are logged in.';
        setTimeout(() => {location.reload(); }, 2000);
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
});