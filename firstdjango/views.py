from django.http import HttpResponse
from django.shortcuts import render


# สร้างฟังก์ชันสำหรับไว้เรียกที่ url.py
def index(request):
    # return HttpResponse("Welcome to my home page")
    return render(request, 'index.html')


def about(request):
    return HttpResponse("This is about page")


# fucntion แบบมี parameter
def search(request, keyword, page):
    return HttpResponse(f'Search for: {keyword} page: {page}')


# function แบบมี query string
def maps(request):
    type = request.GET.get('type', 'hybrid')
    lat = request.GET.get('lat', '13.7245601')
    lon = request.GET.get('lon', '100.4930241')
    zoom = request.GET.get('z', 11)

    return HttpResponse(f"Map type: {type} <br> \
        Location: {lat},{lon}<br> \
        Zoom: {zoom}")


