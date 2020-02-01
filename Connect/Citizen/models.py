from django.db import models
from django.contrib.auth.models import User
from Event.models import Event
from NGO.models import NGO

# Validators 
# from django.core.validators import MaxLengthValidator

class Citizen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    is_volunteer = models.BooleanField(default=False)
    picture = models.ImageField(upload_to="Citizen/Photos")
    events = models.ManyToManyField(Event)
    date_of_joining = models.DateTimeField(auto_now_add=True)
    follows = models.ManyToManyField(NGO)
    points = models.IntegerField(default=10)
    city = models.CharField(max_length=240)
    email = models.EmailField()

    def __str__(self):
        return self.email