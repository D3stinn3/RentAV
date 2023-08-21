from django.urls import path, include
from home import views

# Write your urls here
urlpatterns = [
    path('', views.landingPage, name="landing"),
    path('home/', views.homePage, name="home"),
]
