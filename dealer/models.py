from django.db import models
from home.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from client.models import Area, Vehicles, CarDealer
# Create your models here.
class Customer(models.Model):
    customername = models.OneToOneField(User, on_delete=models.CASCADE)
    customermobile = models.CharField(validators=[MinLengthValidator(10), MaxLengthValidator(13)], max_length=13)
    customerarea = models.ForeignKey(Area, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return self.customername
    
class Orders(models.Model):
    orderuser = models.ForeignKey(User, on_delete=models.PROTECT)
    orderdealer = models.ForeignKey(CarDealer, on_delete=models.PROTECT)
    ordercost = models.CharField(max_length=8)
    ordervehicle = models.CharField(max_length=3)
    is_complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.ordervehicle
    