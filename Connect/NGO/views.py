from django.shortcuts import render
from .ngo_list import get_df
from .models import NGO
from django.http import HttpResponse
import pandas as pd
from .recommend import generate_recommendations

def recommend_ngo(request, title):
    ngo_data = []
    for o in NGO.objects.all():
        ngo_data.append({'Name': o.name, 'Cause': o.cause, 'City': o.cities, 'Details': o.description})
    data = pd.DataFrame(ngo_data)
    recs = generate_recommendations(data, title)
    payload = {
        'NGOS': NGO.objects.all(),
        'Recommendations': recs,
    }
    return render(request, 'aspiration/ngo_list.html', payload)
