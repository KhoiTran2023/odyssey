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
import json


# Page rendering

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

# Tour booking


def register(request):
    return render(request, "odyssey/order.html")


def register_view(request):
    if request.method == "POST":
        try:
            # NEEDS CHANGE
            # p = Passenger(tourChoice = request.POST["tourChoice"], firstName = request.POST["firstName"], lastName = request.POST["lastName"], birthday = request.POST["birthday"], firstNameBill = request.POST["firstNameBill"], lastNameBill = request.POST["lastNameBill"], inputAddress = request.POST["inputAddress"], inputAddress2 = request.POST.get('inputAddress2', ""), inputCity = request.POST["inputCity"], inputState = request.POST["inputState"], inputZip = request.POST["inputZip"], paymentMethod = request.POST["paymentMethod"], cc_name = request.POST["cc-name"], cc_number = request.POST["cc-number"], cc_expiration = request.POST["cc-expiration"], cc_cvv = request.POST["cc-cvv"])
            # p.save()
            messages.success(
                request, "Congratulations! You've successfully booked!")
            return HttpResponseRedirect(reverse('register'))
        except:
            messages.error(request, "Unsuccessful, try again.")
    messages.error(request, "Unsuccessful, try again.")
    return HttpResponseRedirect(reverse('register'))


@csrf_exempt
def fetch_url(request):
    data = {'url1': reverse('index')}
    return JsonResponse(data)

# Authentication System


def registration_view(request):
    return render(request, "odyssey/registration.html")


def create_account(request):
    if request.method == "POST":
        try:
            user = User.objects.create_user(request.POST.get(
                "create-username"), request.POST.get("create-email"), request.POST.get("create-password"))
            user.first_name = request.POST.get("create-user-first-name")
            user.last_name = request.POST.get("create-user-last-name")
            user.save()
            account = Account(user=user, residentialAddress=request.POST.get("create-user-residential-address"), birthday=request.POST.get("create-user-birthday"),
                              socialSecurity=request.POST.get("create-user-social-security"), securityAnswer1=request.POST.get("create-user-security-answer"))
            account.save()
            messages.success(request, "Account Created")
            return render(request, "odyssey/registration.html")
        except:
            return JsonResponse({'status': 'error'}, status=401)


def log_in(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get(
            'username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            # ADD REDIRECT
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error'}, status=401)


def log_out(request):
    logout(request)
    messages.success(request, "logged out")
    return render(request, "odyssey/registration.html")

# CHATBOT


@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        json_data = request.body.decode('utf-8')
        data = json.loads(json_data)
        message = data.get('message')

        # Generate a response
        response = generate_chatbot_response(message)
        # Return the bot's message as a JSON response
        return JsonResponse({'message': response})

    # If the request method is not POST, return an empty response
    return JsonResponse({})


def generate_chatbot_response(message):
    global conversation

    if message.lower() == "hi" or message.lower() == "hello":
        response = "Hi there! How can I help you today?"
    elif "about" in message.lower():
        response = "Odyssey is more than just a trip, it is an experience you will never forget for a lifetime. Experience space from a beautiful itinerary, while in the relief that your safety is guaranteed in our safety training program on top of or extra measures. Welcome to the Future."
    elif "info" in message.lower() or "tour" in message.lower() or "safety" in message.lower() or "program" in message.lower():
        response = "You get to choose from three of the best on Earth flights! To learn more, scroll down on our home page to see our tours, their safety procedures, and how to book them!"
    elif "order" in message.lower() or "status" in message.lower() or "book" in message.lower():
        response = "To book, visit the <strong>Book a Tour</strong> link at the top, you must be logged in. To check on the status of your order, you must be logged in and go into your profile."
    elif "cancel" in message.lower():
        response = "To cancel your order, a representative must cancel it for you. Please visit <strong>Contact Us</strong> to ask us to cancel your order and include a reason why."
    elif "thanks" in message.lower() or "thank you" in message.lower():
        response = "You're welcome! Is there anything else I can assist you with?"
    elif "more" in message.lower() or "help" in message.lower() or "human" in message.lower() or "representative" in message.lower():
        response = "Unfortunately, due to volume, there are no agents available at this time. To have an Odysseynaut help you, visit <strong>Contact Us</strong> to submit a support ticket. Thank you for your patience."
    else:
        response = "I'm sorry, I didn't understand your message. How can I assist you?"
    return response
