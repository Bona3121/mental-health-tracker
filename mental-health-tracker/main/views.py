from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306165603',
        'name': 'Marla Marlena',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)