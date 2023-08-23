from django.urls import path, include
from home import views

# Write your urls here
urlpatterns = [
    path('', views.landingPage, name="landing"),
    path('login/', views.loginPage, name="login"),
    path('signin/', views.signupPage, name="signin"),
    path('account/', views.accountPage, name="account"),
]
