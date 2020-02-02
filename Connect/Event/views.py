from django.shortcuts import render, redirect
from .models import Event
from Citizen.models import Citizen
from .events_rec import rec_events
import pandas as pd
from django.http import HttpResponse

def recommend_event(request, event):
    data = Event.objects.all()
    user = Citizen.objects.filter(user=request.user)[0]
    events_data = []
    events = []
    for d in data:
        events_data.append({
            'Name': d.name, 
            'Purpose': d.purpose
        })
        events.append({
            'id': d.id,
            'name': d.name,
            'date_of_event': d.date_of_event,
            'published': d.published,
            'purpose': d.purpose,
            'rsvp': d.rsvp,
            'event_poster': d.event_poster,
            'tagline': d.tagline,
            'sentiment': d.sentiment,
            'ngo': d.ngo,
            'expected_footfall': d.expected_footfall,
            'price': d.price,
            'location': d.location,
            'difference': d.expected_footfall - d.rsvp,
            'volunteers': len(d.citizen_set.all()),
            'percentage': (d.rsvp//d.expected_footfall)*100,
            'is_volunteer': d in user.events.all()
        })

    events_attending = user.events.all()
    # print(events_attending[0], len(events_attending))
    # print(events_data)
    if len(events_attending) > 0:
        recs = rec_events(pd.DataFrame(events_data), events_attending[0].name if not event else event)
        recs = [Event.objects.filter(name=x)[0] for x in recs]
    else:
        recs = []
    
    payload = {
        'Events': events,
        'Recommendations': recs,
        'User': user,
        'User_events': user.events.all() if user else None,
    }
    print(Event.objects.filter(id=1)[0].citizen_set.all())
    return render(request, 'aspiration/events.html', payload)


def volunteer_event(request, id):
    user = Citizen.objects.filter(user=request.user)[0]
    event = Event.objects.filter(id=id)[0]
    user.events.add(event)
    user.save()
    return redirect('/event/recommend/'+event.name)
