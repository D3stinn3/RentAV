from django.shortcuts import render

# Create your views here.
def homePage(request):
    context = {}
    return render(request, 'hometemp/home.html', context)

def landingPage(request):
    context = {}
    return render(request, 'hometemp/base.html', context)