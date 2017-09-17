from django.shortcuts import render

def index(request):
    return render(request, 'techcrunch/index.html')

def map(request):
    return render(request, 'techcrunch/map.html')
