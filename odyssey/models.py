from django.db import models

# Create your models here.

class Passenger(models.Model):
    tourChoice = models.CharField(max_length = 64)
    firstName = models.CharField(max_length = 64)
    lastName = models.CharField(max_length = 64)
    birthday = models.CharField(max_length = 16)
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

    def __str__(self):
        return f"{self.tourChoice}: {self.lastName}, {self.firstName}"