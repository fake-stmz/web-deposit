from django.shortcuts import render

# Create your views here.
def index(request):


    dep_sum = request.GET.get('dep-sum', '')
    dur = request.GET.get('duration', '')
    tarif = request.GET.get('tarif', '')
    percent = 10
    res_sum = float(dep_sum) if dep_sum else 0
    profit = 0

    if dep_sum and dur and tarif:

        if tarif == "Лучший": percent = 20
        if tarif == "Просто космос": percent = 30

        for i in range(int(dur)): res_sum += res_sum * percent * 0.01

        profit = res_sum - float(dep_sum)

    context = {
        'dep_sum': dep_sum,
        'dur': dur,
        'tarif': tarif,
        'percent': percent,
        'res_sum': res_sum,
        'profit': profit
    }

    return render(request, "index.html", context)