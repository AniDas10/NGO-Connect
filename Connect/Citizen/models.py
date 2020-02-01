from django.db import models
from django.contrib.auth.models import User
from Event.models import Event

# Validators 
# from django.core.validators import MaxLengthValidator

class Citizen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    is_volunteer = models.BooleanField(default=False)
    picture = models.ImageField(upload_to="Citizen/Photos")
    events = models.ManyToManyField(Event)
    date_of_joining = models.DateTimeField(auto_now_add=True)