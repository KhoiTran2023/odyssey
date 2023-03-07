var prevScrollpos = window.pageYOffset;
function navbarScroll() {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        document.getElementById("navbar").style.top = "0";
        document.getElementById("chat-toggle").style.right = "50px";
    } else {
        document.getElementById("chat-toggle").style.right = "-100px";
        document.getElementById("navbar").style.top = "-100px";
    }
    prevScrollpos = currentScrollPos;
}

function scrollFunction() {
    if (document.body.scrollTop > 700 || document.documentElement.scrollTop > 700) {
        document.getElementById("navbar").style.backdropFilter = "blur(1rem)";
        document.getElementById("navbar").style.background = "hsl(0 0% 100% / 0.1)";
    } else {
        document.getElementById("navbar").style.backdropFilter = "none";
        document.getElementById("navbar").style.background = "none";

    }
}

function toggleChat() {
    var chat = document.getElementById("chat-container");
    if(chat.style.display == "block")
    {
        chat.style.display = "none";
        chat.classList.toggle("animate-expand");
    }
    else
    {
        chat.style.display = "block";
        chat.classList.toggle("animate-expand");
    }
}