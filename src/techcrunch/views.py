from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

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
            return redirect('techcrunch/index')
    else:
        form = UserCreationForm()
    return render(request, 'techcrunch/signup.html', {'form': form})

def map(request):
	# r = requests.get('http://www.mapquestapi.com/directions/v2/route?key=UShjaMayAC4UkuBJ5nu5rqFuraxzEOQU' + 
	# 				'&from=San Francisco, CA&to=Oakland,+CA')
	# r = requests.get('http://www.mapquestapi.com/geocoding/v1/batch?key=UShjaMayAC4UkuBJ5nu5rqFuraxzEOQU' +
	# 				'&location=San Francisco,CA&location=Oakland,CA&location=Milbrae,CA')
    return render(request, 'techcrunch/map.html')

def shelter_routing(request):
    return render(request, 'techcrunch/shelter_routing.html')
