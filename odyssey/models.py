from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    residentialAddress = models.CharField(max_length = 100)
    birthday = models.CharField(max_length = 16)
    socialSecurity = models.CharField(max_length = 20)
    securityAnswer1 = models.CharField(max_length = 64)

class Payment(models.Model):
    firstNameBill = models.CharField(max_length = 64)
    lastNameBill = models.CharField(max_length = 64)
    inputAddress = models.CharField(max_length = 64)
    inputAddress2 = models.CharField(max_length = 64, null = True)
    inputCity = models.CharField(max_length = 64)
    inputState = models.CharField(max_length = 64)
    inputZip = models.CharField(max_length = 64)
    paymentMethod = models.CharField(max_length = 64)
    cc_name = models.CharField(max_length = 64)
    cc_number = models.CharField(max_length = 64)
    cc_expiration = models.CharField(max_length = 64)
    cc_cvv = models.CharField(max_length = 64)
    account = models.ForeignKey(User, on_delete=models.CASCADE)

STATUS_CHOICES = (
    ("pending", "pending"),
    ("failed", "failed"),
    ("processed", "processed"),
    ("reviewing", "reviewing"),
    ("approved", "approved"),
    ("completed", "completed"),
)

class Booking(models.Model):
    tourChoice = models.CharField(max_length = 64)
    passengerFirstName = models.CharField(max_length = 64)
    passengerLastName = models.CharField(max_length = 64)
    birthday = models.CharField(max_length = 16)
    socialSecurity = models.CharField(max_length = 20)
    payment = models.ForeignKey(Payment, on_delete = models.CASCADE)
    account = models.ForeignKey(User, on_delete = models.CASCADE)
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = "pending",
    )

    def __str__(self):
        return f"{self.tourChoice}: {self.lastName}, {self.firstName}"