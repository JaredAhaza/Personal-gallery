from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image


# Create your views here.
def welcome(request):
    date = dt.date.today
    photos = Image.get_all()
    return render(request, 'welcome.html',{"date": date,"photos": photos})

def image(request, image_id):
    image = Image.get_image(image_id)
    print(image.image.url)
    return render(request, 'all-images/image.html', {"image": image})


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        query = request.GET.get("image")
        results = Image.searched(query)
        message = f"{query}"

        return render(request, 'all-images/search.html',{"message": message, "results": results})
    else:
        message = "What images do you want to search for?"
        return render(request, 'all-images/search.html',{"message": message})


def get_kenya(request):
    location_images = Image.kenya()
    return render(request, 'all-images/locations.html', {"images": location_images})