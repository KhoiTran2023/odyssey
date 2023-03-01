from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from odyssey.models import *
from django.contrib.auth import authenticate, login, logout

#Page rendering

def index(request):
    return render(request, "odyssey/index.html")


def sources(request):
    return render(request, "odyssey/sources.html")

def safety(request):
    return render(request, "odyssey/safety.html")


def contact_us(request):
    return render(request, "odyssey/contactus.html")

def error(request):
    return render(request, "odyssey/error.html")

#Tour booking

def register(request):
    return render(request, "odyssey/order.html")

def register_view(request):
    if request.method == "POST":
        try:
            #NEEDS CHANGE
            #p = Passenger(tourChoice = request.POST["tourChoice"], firstName = request.POST["firstName"], lastName = request.POST["lastName"], birthday = request.POST["birthday"], firstNameBill = request.POST["firstNameBill"], lastNameBill = request.POST["lastNameBill"], inputAddress = request.POST["inputAddress"], inputAddress2 = request.POST.get('inputAddress2', ""), inputCity = request.POST["inputCity"], inputState = request.POST["inputState"], inputZip = request.POST["inputZip"], paymentMethod = request.POST["paymentMethod"], cc_name = request.POST["cc-name"], cc_number = request.POST["cc-number"], cc_expiration = request.POST["cc-expiration"], cc_cvv = request.POST["cc-cvv"])
            #p.save()
            messages.success(
                request, "Congratulations! You've successfully booked!")
            return HttpResponseRedirect(reverse('register'))
        except:
            messages.error(request, "Unsuccessful, try again.")
    messages.error(request, "Unsuccessful, try again.")
    return HttpResponseRedirect(reverse('register'))

#Authentication System
def create_account(request):
    if request.method == "POST":
        try:
            user = User.objects.create_user(request.POST["username"],request.POST["emailAddress"], request.POST["password"])
            user.first_name = request.POST["userFirstName"]
            user.last_name = request.POST["userLastName"]
            user.save()
            account = Account(user = user, residentialAddress = request.POST["userResidentialAddress"], birthday = request.POST["userBirthday"], socialSecurity = request.POST["userSocialSecurity"], securityAnswer1 = request.POST["userSecurityQuestion"])
            account.save()
        except:
            messages.error(request, "Unsuccessful, try again.")

def log_in(request):
    user = authenticate(request, username = request.POST["username"], password = request.POST["password"])
    if user is not None:
        login(request, user)
        #ADD REDIRECT
        HttpResponseRedirect(reverse("register"))
    else:
        messages.error(request, "Incorrect username/password, try again.")
        HttpResponseRedirect(reverse("register"))

def log_out(request):
    logout(request)
    HttpResponseRedirect(reverse("register"))