from django.shortcuts import render
from .forms import UserRegisterForm


def home(request):
    return render(request, 'frontend/index.html')


def login(request):
    return render(request, 'frontend/login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'frontend/register.html', context)
