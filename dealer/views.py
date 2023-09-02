from django.shortcuts import render, redirect
from client.models import Area, CarDealer, Vehicles
from home.models import User
from dealer.models import Orders, Customer

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
    context = {}
    return render(request, 'dealertemp/vehicleupdate.html', context)

def manageVehicle(request):
    username = request.user
    user = User.objects.get(username=username)
    vehicleDealer = CarDealer.objects.get(vehicledealer=user)
    vehicleList = []
    vehicles = Vehicles.objects.filter(vehicledealer=vehicleDealer)
    for vehicle in vehicles:
        vehicleList.append(vehicle)
    context = {'vehiclelist': vehicleList}
    return render(request, 'dealertemp/manage.html', context)

def orderList(request):
    username = request.user
    user = User.objects.get(username=username)
    vehicleDealer = CarDealer.objects.get(dealer=user)
    orders = Orders.objects.filter(orderdealer=vehicleDealer)
    orderList = []
    for order in orders:
        if order.is_complete == False:
            orderList.append(order)
    context = {'orderlist': orderList}
    return render(request, 'dealertemp/orderlist.html', context)
    
def completeOrder(request):
    orderID = request.POST['id']
    order = Orders.objects.get(id=orderID)
    
    vehicle = order.vehicle
    order.is_complete = True
    order.save()
    vehicle.is_available = True
    vehicle.save()
    return redirect('orderlist')

def historyOrder(request):
    user = User.objects.get(username=request.user)
    vehicleDealer = CarDealer.objects.get(dealer=user)
    
    orders = Orders.objects.filter(orderdealer=CarDealer)
    orderList = []
    
    for order in orders:
        orderList.append(order)
    
    context = {'wallet': vehicleDealer.wallet, 'orderlist': orderList}
    return render(request, 'dealertemp/history.html', context)

def delete(request):
    vehicleID = request.POST['id']
    vehicle = Vehicles.objects.get(id=vehicleID)
    
    vehicle.delete()
    return redirect('managevehicles')