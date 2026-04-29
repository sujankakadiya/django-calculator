from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render


def calculator(request):
    c = ''
    n1 = ''
    n2 = ''

    try:
        if request.method == "POST":
            n1 = float(request.POST.get('num1'))
            n2 = float(request.POST.get('num2'))
            opr = request.POST.get('opr')

            if opr == '+':
                c = n1 + n2
            elif opr == '-':
                c = n1 - n2
            elif opr == '*':
                c = n1 * n2
            elif opr == '/':
                c = n1 / n2 if n2 != 0 else "Cannot divide by zero"

    except:
        c = "Invalid Input"

    return render(request, 'calculator.html', {
        'c': c,
        'n1': n1,
        'n2': n2
    })


