from django.urls import path, include
from client import views

urlpatterns = [
    path('search/', views.search, name="search"),
    path('searchresults/', views.searchResults, name="searchresult"),
]
