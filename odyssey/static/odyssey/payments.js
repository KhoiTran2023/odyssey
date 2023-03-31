const popupForm = document.getElementById("payment-form-popup");
const orderForm = document.getElementById("orderForm");
const npForm = document.getElementById("add-payment-form");

function toggleSavedToPay() {
    if (popupForm.style.display == "none") {
        popupForm.style.display = "block";
        npForm.style.display = "none";
    }
    else {
        popupForm.style.display = "none";
    }
}

function toggleSavedToPay(tourChoice) {
    if (popupForm.style.display == "none") {
        popupForm.style.display = "block";
        npForm.style.display = "none";
        let string = tourChoice
        document.getElementById("Individual-Value").value = string;
    }
    else {
        popupForm.style.display = "none";
    }
}

function submitPayment() {

    const formData = new FormData(orderForm);

    fetch('/register/submit', {
        method: 'POST',
        body: formData
    })
        .then(response => {
            if (response.status === 200) {
            } else {
            }
        })
        .catch(error => {
            console.error(error);
        });
}

function toggleAddNewPayment() {
    if (npForm.style.display == "none") {
        npForm.style.display = "block";
        popupForm.style.display = "none";
    }
    else {
        popupForm.style.display = "block";
        npForm.style.display = "none";
    }
}

function addNewPayment() {
    const formData = new FormData(npForm);

    fetch('/add-payment', {
        method: 'POST',
        body: formData
    })
        .then(response => {
            if (response.status === 200) {
                location.reload();
            } else {
            }
        })
        .catch(error => {
            console.error(error);
        });
}

function changeNumTickets(numTickets) {
    var value = numTickets.value;
    document.getElementById("num-tickets").value = value;
}

function changeDate(departDate) {
    var value = departDate.value;
    document.getElementById("tickets-date").value = value;
}