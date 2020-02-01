from django.shortcuts import render, redirect
from .ngo_list import get_df
from .models import NGO
from django.http import HttpResponse
import pandas as pd
from .recommend import generate_recommendations
from Citizen.models import Citizen

def recommend_ngo(request, title):
    ngo_data = []
    user = Citizen.objects.filter(user=request.user)[0]
    ngos = []
    for o in NGO.objects.all():
        ngo_data.append({'Name': o.name, 'Cause': o.cause, 'City': o.cities, 'Details': o.description})

        ngos.append({
            'id': o.id,
            'name': o.name,
            'cause': o.cause,
            'cities': o.cities,
            'description': o.description,
            'website_link': o.website_link,
            'logo': o.logo,
            'categories': o.categories,
            'email': o.email,
            'is_following': o in user.follows.all()
        })
    data = pd.DataFrame(ngo_data)
    recs = generate_recommendations(data, title)
    recs = [NGO.objects.filter(name=x)[0] for x in recs]

    ngos_following = user.follows.all()
    if len(ngos_following) > 0:
        recs = generate_recommendations(data, ngos_following[0].name if not title else title)
        recs = [NGO.objects.filter(name=x)[0] for x in recs]
    else:
        recs = []

    payload = {
        'NGOS': ngos,
        'Recommendations': recs,
    }
    return render(request, 'aspiration/ngo_list.html', payload)


def follow_ngo(request, id):
    user = Citizen.objects.filter(user=request.user)[0]
    ngo = NGO.objects.filter(id=id)[0]
    user.follows.add(ngo)
    user.save()
    return redirect('/ngo/'+ngo.name)


def ngo_login(request):
    return render(request, 'aspiration/login.html')

def ngo_register(request):
    return render(request, 'aspiration/ngo_reg.html')