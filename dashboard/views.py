from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    # return render(request, 'dashboard.html')
    return HttpResponse('This is the Dashboard')
