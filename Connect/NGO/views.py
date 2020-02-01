from django.shortcuts import render
from .ngo_list import get_df
from .models import NGO
from django.http import HttpResponse
# Create your views here.

def populate_once(request):
    data = get_df()
    for d in data:
        ngo_object = NGO(name=d['Name'], cause=d['Cause'], cities=d['City'], description=d['Details'], website_link=d['Link'])
        ngo_object.save()
    return HttpResponse('Done')
