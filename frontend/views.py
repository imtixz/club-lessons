from django.shortcuts import render
from .forms import UserRegisterForm, ProfileRegisterForm, loginForm


def home(request):
    return render(request, 'frontend/index.html')


def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

    form = loginForm()
    context = {'form': form}
    return render(request, 'frontend/login.html', context)


def register(request):
    if request.method == 'POST':
        uform = UserRegisterForm(request.POST)
        pform = ProfileRegisterForm(request.POST)
        if uform.is_valid() and pform.is_valid():
            new_user = uform.save(commit=False)
            uform.save()
            pform = ProfileRegisterForm(
                request.POST, instance=new_user.profile)
            pform.save()
            # add a message saying ur account has been created
            # redirect to the login page
    else:
        uform = UserRegisterForm()
        pform = ProfileRegisterForm()

    context = {'uform': uform, 'pform': pform}
    return render(request, 'frontend/register.html', context)
