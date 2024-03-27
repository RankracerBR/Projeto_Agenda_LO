from django.shortcuts import render

# Create your views here.

variavel = 1

def index(request):
    return render(
        request,
        'contact/index.html',
    )