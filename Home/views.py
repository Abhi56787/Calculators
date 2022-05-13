from typing import OrderedDict
from django.http import request
from django.shortcuts import render, HttpResponse

# Create your views here.
def __format_currency(curr:str | float | int) -> str:
    if type(curr) != str:
        curr = str(curr)

    new = curr[-1:-4:-1][::-1]
    curr = curr[-4::-1][::-1]

    ele_list = []
    curr = '0'+curr if len(curr)%2!=0 else curr
    i = 0
    while i < len(curr):
        ele_list.append(curr[i:i+2])
        i+=2
    ele_list.append(new)
    curr = ','.join(ele_list)
    return curr.removeprefix('0')


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

        total_amt = __format_currency(f'{int(total_amt)}')
        amt_inv = __format_currency(f'{int(amt_inv)}')
        profit = __format_currency(f'{int(profit)}')
        total_return = __format_currency(f'{int(total_return)}')

        result = f'Total Earning : ₹ {total_amt}<br>Amount Invested : ₹ {amt_inv}<br>Profit : ₹ {profit}<br>Total Return : {total_return} %'
        context = {
            'result' : result,
        }
        return render(request, 'result.html', context)

    return render(request, 'monthly_investment.html')



def vis_time(request):
    if request.method == 'POST':
        try:
            amt = float(request.POST.get('amount'))
            mon_inv = float(request.POST.get('monthly_investment'))
            exp_ret = float(request.POST.get('exp_ret'))
        except Exception:
            return render(request, 'result.html', context={'result' : 'Enter Valid Values'})

        mon_inv *= 12
        total_amt = mon_inv + (mon_inv * exp_ret) / 100
        years = 1
        while total_amt < amt:
            years += 1 
            temp = total_amt + mon_inv
            temp += temp * exp_ret / 100
            total_amt = temp
        
        amount_inv = mon_inv * years
        profit = total_amt - amount_inv
        total_ret = (total_amt - amount_inv) * 100 / amount_inv

        total_amt = __format_currency(int(total_amt))
        amount_inv = __format_currency(int(amount_inv))
        profit = __format_currency(int(profit))
        total_ret = __format_currency(int(total_ret))

        result = f'Amount can be earned : ₹{total_amt} in {years} years <br>Amount Invested : ₹{amount_inv}<br>Profit : ₹{profit} <br>Total Return : {total_ret}%'
        return render(request, 'result.html', context={'result' : result})

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

            total_amt = __format_currency(int(total_amt))
            amt_inv = __format_currency(int(amt_inv))
            profit = __format_currency(int(profit))
            total_ret = __format_currency(int(total_ret))

            result = f'Total Earning after {years} years: ₹{total_amt}<br>Amount Invested : ₹{amt_inv}<br>Profit : ₹{profit}<br>Amount Return : {total_ret}%'
            return render(request, 'result.html', {'result' : result})
        except Exception:
            return render(request, 'result.html', {'result':'Enter Valid values'})

    return render(request, 'step_up_mon_inv.html')


def vis_time_up(request):
    if request.method == 'POST':
        try:
            amt = float(request.POST.get('amount'))
            mon_inv = float(request.POST.get('monthly_investment'))
            mon_inc = float(request.POST.get('monthly_increment'))
            exp_ret = float(request.POST.get('exp_ret'))
        except Exception:
            return render(request, 'result.html', context={'result' : 'Enter Valid Values'})

        mon_inv *= 12
        amt_inv = 0
        amt_inv += mon_inv
        total_amt = mon_inv + (mon_inv * exp_ret) / 100
        years = 1
        while total_amt < amt:
            mon_inv += mon_inc * 12
            amt_inv += mon_inv
            years += 1 
            temp = total_amt + mon_inv
            temp += temp * exp_ret / 100
            total_amt = temp
        
        profit = total_amt - amt_inv
        total_ret = (total_amt - amt_inv) * 100 / amt_inv

        total_amt = __format_currency(int(total_amt))
        amt_inv = __format_currency(int(amt_inv))
        profit = __format_currency(int(profit))
        total_ret = __format_currency(int(total_ret))

        result = f'Amount can be earned : ₹{total_amt} in {years} years <br>Amount Invested : ₹{amt_inv}<br>Profit : ₹{profit} <br>Total Return : {total_ret}%'
        return render(request, 'result.html', {'result' : result})

    return render(request, 'vis_time_up.html')

