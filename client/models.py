from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator 
from home.models import User

# Create your models here.
class Area(models.Model):
    areacode = models.CharField(validators=[MinLengthValidator(7), MaxLengthValidator(7)], max_length=7, unique=True)
    city = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.areacode
    
class CarDealer(models.Model):
    dealer = models.OneToOneField(User, on_delete=models.CASCADE)
    dealermobile = models.CharField(validators=[MinLengthValidator(10), MaxLengthValidator(13)], max_length=13)
    dealerarea = models.OneToOneField(Area, on_delete=models.PROTECT)
    dealerwallet = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.dealer
    
class Vehicles(models.Model):
    vehiclename = models.CharField(max_length=20)
    vehiclemodel = models.CharField(max_length=20)
    vehicleyear = models.DateField()
    vehiclecapacity = models.CharField(max_length=100)
    vehicledealer = models.ForeignKey(CarDealer, on_delete=models.PROTECT)
    vehiclearea = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
    is_available = models.BooleanField(default=True)
    vehicledescription = models.CharField(max_length=100)
    vehiclecostperday = models.CharField(max_length=50)
    vehicledescription = models.TextField()
    vehiclelike = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.vehiclename