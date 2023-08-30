from django.shortcuts import render
from client.models import Area, CarDealer, Vehicles

# Create your views here.
def addVehicle(request):
    vehicleName = request.POST['vehiclename']
    vehicleCapacity = request.POST['vehiclecapacity']
    vehicleDescription = request.POST['vehicledescription']
    vehicleYear = request.POST['vehicleyear']
    vehicleModel = request.POST['vehiclemodel']
    vehicleDescription = request.POST['vehicledescription']
    vehicleCostperday = request.POST['vehiclecostperday']
    vehicleArea = request.POST['vehiclearea']
    vehiclePincode = request.POST['vehiclepincode']
    vehicleCity = request.POST['city']
    vehicleDealer = CarDealer.objects.get(dealer=request.user)
    try:
        area = Area.objects.get(city=vehicleCity, pincode=vehiclePincode)
    except:
        area = None
        
    if area is not None:
        vehicle = Vehicles(vehiclename=vehicleName, vehiclemodel=vehicleModel, vehicledealer=vehicleDealer, vehiclearea=vehicleArea, vehicledescription=vehicleDescription, vehiclecapacity=vehicleCapacity)
    else:
        area = Area(city=vehicleCity, pincode=vehiclePincode)
        area.save()
        area = Area.objects.get(city=vehicleCity, pincode=vehiclePincode)
        vehicle = Vehicles(vehiclename=vehicleName, vehiclemodel=vehicleModel, vehicledealer=vehicleDealer, vehiclearea=vehicleArea, vehicledescription=vehicleDescription, vehiclecapacity=vehicleCapacity)
    vehicle.save()
    return render(request, 'dealertemp/vehicleupdate.html')