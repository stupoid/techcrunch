from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from techcrunch.models import Shelter

def index(request):
    return render(request, 'techcrunch/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('techcrunch/index.html')
    else:
        form = UserCreationForm()
    return render(request, 'techcrunch/signup.html', {'form': form})

def create_shelter(request):
    if request.method == 'POST':
        name = request.POST['name']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        max_occupancy = request.POST['max_occupancy']
        is_hq = 'is_hq' in request.POST.getlist('is_hq')
        shelter = Shelter.objects.create(name=name,latitude=latitude,longitude=longitude, max_occupancy=max_occupancy)
        if is_hq:
            shelter.hq_id = shelter.id
    return render(request, 'techcrunch/create-shelter.html')

def dashboard(request):
    return render(request, 'techcrunch/dashboard.html')

def residents(request):
    return render(request, 'techcrunch/residents.html')

def nearby_shelters(request):
    return render(request, 'techcrunch/nearby_shelters.html')

def map(request):
	# r = requests.get('http://www.mapquestapi.com/directions/v2/route?key=UShjaMayAC4UkuBJ5nu5rqFuraxzEOQU' +
	# 				'&from=San Francisco, CA&to=Oakland,+CA')
	# r = requests.get('http://www.mapquestapi.com/geocoding/v1/batch?key=UShjaMayAC4UkuBJ5nu5rqFuraxzEOQU' +
	# 				'&location=San Francisco,CA&location=Oakland,CA&location=Milbrae,CA')
    return render(request, 'techcrunch/map.html')

def shelter_routing(request):
    return render(request, 'techcrunch/shelter_routing.html')
