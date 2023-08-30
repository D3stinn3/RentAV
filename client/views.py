from django.shortcuts import render
from home.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from client.models import Area, Vehicles

# Create your views here.
def index(request):
    context = {}
    if not request.user.is_authenticated:
        return render(request, 'hometemp/login.html', context)
    else:
        return render(request, 'hometemp/signin.html', context)
    
def search(request):
    context = {}
    return render(request, 'clienttemp/search.html', context)

def searchResults(request):
    city = request.POST['city']
    city = city.lower()
    vehicleList = []
    areas = Area.objects.get(city=city)
    for area in areas:
        vehicles = Vehicles.objects.filter(area=area)
        for vehicle in vehicles:
            if vehicle.is_available == True:
                vehicleDict = {'name': vehicle.vehiclename, 'model': vehicle.vehiclemodel, 'id': vehicle.id, 'capacity': vehicle.vehiclecapacity, 'description': vehicle.vehicledescription}
                vehicleList.append(vehicleDict)
    request.session['vehiclelist'] = vehicleList
    return render(request, 'clienttemp/searchresults.html')