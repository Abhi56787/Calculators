from django.http import request
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home.html')


def monthly_investment(request):
    return render(request, 'monthly_investment.html')

def vis_time(request):
    return render(request, 'vis_time.html')

def step_up_mon_inv(request):
    return render(request, 'vis_time.html')

def vis_time_up(request):
    return render(request, 'vis_time.html')

