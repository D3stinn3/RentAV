from django.urls import path, include
from home import views

# Write your urls here
urlpatterns = [
    path('', views.landingPage, name="landing"),
    path('login/', views.loginPage, name="login"),
    path('signin/', views.signupPage, name="signin"),
    path('dealer/', views.dealerPage, name="dealer"),
    path('client/', views.clientPage, name="client"),
]
