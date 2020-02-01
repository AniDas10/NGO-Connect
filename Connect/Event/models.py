from django.db import models
from NGO.models import NGO

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=120)
    date_of_event = models.DateTimeField()
    published = models.DateTimeField(auto_now_add=True)
    purpose = models.TextField()
    rsvp = models.IntegerField(default=0)
    event_poster = models.ImageField(upload_to='Events/Posters')
    tagline = models.CharField(max_length=540)
    sentiment = models.IntegerField(default=0)
    ngo = models.OneToOneField(NGO)
    expected_footfall = models.BigIntegerField()
    price = models.IntegerField(default=0)