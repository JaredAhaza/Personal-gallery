from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
import datetime as dt


# Create your views here.
def welcome(request):
    #return HttpResponse('Welcome to my personal gallery')
    return render(request, 'welcome.html')
def gallery_today(request):
    date = dt.date.today()
    image = Image.get_image(image_id)
    return render(request, 'all-images/today-images.html', {"date": date}, {"image": image})

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


    image = Image.get_image(image_id)
    return render(request, 'all-images/past-images.html', {"date": date}, {"image": image})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        query = request.GET.get("image")
        results = Image.searched(query)
        message = f"{query}"

        return render(request, 'all-images/search.html',{"message": message, "results": results})
    else:
        message = "What images do you want to search for?"
        return render(request, 'all-images/search.html',{"message": message})


def get_cars(request):
    location_images = Image.cars()
    return render(request, 'all-images/locations.html', {"images": location_images})


def get_myhood(request):
    location_images = Image.myhood()
    return render(request, 'all-images/locations.html', {"images": location_images})


def get_videogames(request):
    location_images = Image.videogames()
    return render(request, 'all-images/locations.html', {"images": location_images})
