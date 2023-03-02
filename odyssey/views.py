from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from odyssey.models import *
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random
import re

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

#CHATBOT
def process_message(message):
    # Define a list of possible responses
    responses = [
        "I'm sorry, I didn't understand that.",
        "Could you please rephrase that?",
        "I'm not sure what you mean. Can you give me more information?",
        "Thanks for your message! Our team will get back to you as soon as possible.",
    ]

    # Define regular expressions to search for keywords in the message
    hello_pattern = re.compile(r"\bhello\b|\bhi\b|\bhey\b", re.IGNORECASE)
    pricing_pattern = re.compile(r"\bpricing\b", re.IGNORECASE)
    support_pattern = re.compile(r"\bsupport\b|\bhelp\b", re.IGNORECASE)

    # Check if the message matches any of the patterns and generate a specific response
    if hello_pattern.search(message):
        response = "Hello! How can I assist you today?"
    elif pricing_pattern.search(message):
        response = "Please visit our pricing page at book a tour for more information."
    elif support_pattern.search(message):
        response = "You can contact our support team at the contact page for assistance."
    else:
        # Select a random response from the list
        response = random.choice(responses)

    return response

@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        # Get the user message from the request body
        message = request.POST.get("message", "bingbog")
        print(message)
        # Use a chatbot API or logic to generate a response
        response = process_message(message)

        # Return the response as a JSON object
        return JsonResponse({"response": response})

    # Return an empty response if the request method is not POST
    return JsonResponse({})