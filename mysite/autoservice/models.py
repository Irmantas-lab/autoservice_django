from django.db import models

# Create your models here.
class Car_Order (models.Model):
    name = models.CharField ('Pavadinimas', max_length=200, help_text="Iveskite zanra (pvz. detektyvas)")

class Car_Model (models.Model):
    name = models.CharField ('Modelis', max_length=100)

