from typing import OrderedDict
from django.http import request
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home.html')


def monthly_investment(request):
    if request.method == 'POST':
        try:
            mon_inv = float(request.POST.get('monthly_investment'))
            years = int(request.POST.get('years'))
            exp_ret = float(request.POST.get('exp_ret'))
        except Exception:
            return render(request, 'result.html', {'result':'Enter Valid values'})
        
        mon_inv *= 12
        total_amt = mon_inv + (mon_inv * exp_ret / 100)

        for _ in range(1,years):
            temp = total_amt + mon_inv
            temp += (temp * exp_ret) / 100
            total_amt = temp

        amt_inv = mon_inv * years
        total_return = (total_amt - amt_inv)*100/amt_inv
        profit = total_amt - amt_inv

        result = f'Total Earning : ₹ {total_amt:.2f}<br>Amount Invested : ₹ {amt_inv:.2f}<br>Profit : ₹ {profit:.2f}<br>Total Return : {total_return:.2f} %'
        context = {
            'result' : result,
        }
        return render(request, 'result.html', context)

    return render(request, 'monthly_investment.html')



def vis_time(request):
    if request.method == 'POST':
        return HttpResponse(request)    
    return render(request, 'vis_time.html')


def step_up_mon_inv(request):
    if request.method == 'POST':
        try:
            mon_inv = float(request.POST.get('monthly_investment'))
            mon_inc = float(request.POST.get('monthly_inc'))
            years = int(request.POST.get('years'))
            exp_ret = float(request.POST.get('exp_ret'))

            mon_inv *= 12
            amt_inv = mon_inv 
            total_amt = mon_inv + (mon_inv * exp_ret) / 100
            for _ in range(1,years):
                mon_inv += mon_inc * 12
                amt_inv += mon_inv 
                total_val = total_amt + mon_inv
                total_val += (total_val * exp_ret)/100
                total_amt = total_val

            profit = total_amt - amt_inv
            total_ret = (total_amt - amt_inv) * 100 / amt_inv 
            result = f'Total Earning after {years} years: ₹{total_amt:.2f}<br>Amount Invested : ₹{amt_inv:.2f}<br>Profit : ₹{profit:.2f}<br>Amount Return : {total_ret:.2f}%'
            return render(request, 'result.html', {'result' : result})
        except Exception:
            return render(request, 'result.html', {'result':'Enter Valid values'})

        return HttpResponse(request)    
    return render(request, 'step_up_mon_inv.html')


def vis_time_up(request):
    if request.method == 'POST':
        return HttpResponse(request)    
    return render(request, 'vis_time_up.html')

