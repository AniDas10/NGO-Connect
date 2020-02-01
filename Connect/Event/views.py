from django.shortcuts import render
from .models import Event
from .events_rec import rec_events
import pandas as pd
from django.http import HttpResponse

def recommend_event(request, event):
    data = Event.objects.all()
    events_data = []
    for d in data:
        events_data.append({'Name': d.name, 'Purpose': d.purpose})
    recs = rec_events(pd.DataFrame(events_data), event)
    payload = {
        'Events': data,
        'Recommendations': recs
    }
    return render(request, 'aspiration/events.html', payload)