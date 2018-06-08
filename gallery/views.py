from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
import datetime as dt


# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to my personal gallery')


def gallery_today(request):
    date = dt.date.today()
    
    return render(request, 'all-images/today-images.html', {"date": date,"gallery": gallery})

def convert_dates(dates):
    #function that gets weekday number for the date
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    #returning the actual day of the week
    day = days[day_number]
    return day

def past_days_gallery(request,past_date):

    try:
        # Converts data from the string url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 when value error is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(gallery_today)

    
    return render(request, 'all-images/past-images.html', {"date": date,"gallery": gallery})
