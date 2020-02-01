from django.db import models

class City(models.Model):
    name = models.CharField(max_length=120)

class Blog(models.Model):
    title = models.CharField(max_length=250)
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE)

class NGO(models.Model):
    CATEGORIES = [
        ('Health', 'Health'),
        ('Education', 'Education'),
        ('Women Empowerment', 'Women Empowerment'),
        ('Children', 'Children'),
        ('Senior Citizens', 'Senior Citizens'),
        ('Others', 'Others')
    ]

    name = models.CharField(max_length=250)
    cause = models.TextField()
    cities = models.ManyToManyField(City)
    description = models.TextField()
    website_link = models.URLField(max_length=520)
    logo = models.ImageField(upload_to='NGOs/Logos')
    blogs = models.ManyToManyField(Blog)
    categories = models.CharField(choices=CATEGORIES)

class Similar(models.Model):
    ngo = models.PrimaryKey(NGO, on_delete=models.CASCADE)
    similars = models.ForeignKey(NGO)
