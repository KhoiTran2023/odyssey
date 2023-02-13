from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from odyssey.models import Passenger


def index(request):
    return render(request, "odyssey/index.html")


def sources(request):
    return render(request, "odyssey/sources.html")


def register(request):
    return render(request, "odyssey/order.html")

# Needs to update google spreadsheet


def isEmptyData(row):
    return sheet.cell(row, 1).value is None


def register_view(request):
    if request.method == "POST":
        p = Passenger(tourChoice = request.POST["tourChoice"], firstName = request.POST["firstName"], lastName = request.POST["lastName"], birthday = request.POST["birthday"], firstNameBill = request.POST["firstNameBill"], lastNameBill = request.POST["lastNameBill"], inputAddress = request.POST["inputAddress"], inputAddress2 = request.POST.get('inputAddress2', ""), inputCity = request.POST["inputCity"], inputState = request.POST["inputState"], inputZip = request.POST["inputZip"], paymentMethod = request.POST["paymentMethod"], cc_name = request.POST["cc-name"], cc_number = request.POST["cc-number"], cc_expiration = request.POST["cc-expiration"], cc_cvv = request.POST["cc-cvv"])
        p.save()
        messages.success(
            request, "Congratulations! You've successfully booked!")
        return HttpResponseRedirect(reverse('register'))
    messages.error(request, "Unsuccessful, try again.")
    return HttpResponseRedirect(reverse('register'))


def safety(request):
    return render(request, "odyssey/safety.html")


def contact_us(request):
    return render(request, "odyssey/contactus.html")
