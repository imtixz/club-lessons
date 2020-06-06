from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileRegisterForm, loginForm
from backend.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def getGrad(current_year):
    # helper function
    return current_year


@login_required
def home(request):
    return render(request, 'frontend/index.html')


@login_required
def beginner(request):
    return render(request, 'frontend/beginner.html')


@login_required
def novice(request):
    return render(request, 'frontend/novice.html')


@login_required
def openV(request):
    return render(request, 'frontend/open.html')


@login_required
def advanced(request):
    return render(request, 'frontend/advanced.html')


def user_login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            rcdc_password = form.cleaned_data['rcdc_password']
            if rcdc_password == 'realrcdcmember':
                user = authenticate(
                    request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(
                        request, "You have successfully logged in.")
                    return redirect('home')
                else:
                    messages.warning(
                        request, "Wrong login credentials entered. Please enter a valid username and password.")
                    return redirect('login')
            else:
                messages.warning(
                    request, "You entered the wrong rcdc password.")
                return redirect('login')
        else:
            return messages.warning(request, "Wrong login credentials entered. Please enter a valid username and password.")

    form = loginForm()
    context = {'form': form}
    return render(request, 'frontend/login.html', context)


def user_logout(request):
    logout(request)
    return render(request, 'frontend/logout.html')


def register(request):
    if request.method == 'POST':
        uform = UserRegisterForm(request.POST)
        pform = ProfileRegisterForm(request.POST)
        if uform.is_valid() and pform.is_valid():
            new_username = uform.cleaned_data['username']
            uform.save()
            new_user = User.objects.get(username=new_username)
            pdata = pform.cleaned_data
            account = Profile(
                user=new_user, fname=pdata['fname'], lname=pdata['lname'], number=pdata['number'],
                address=pdata['address'], gender=pdata['gender'],
                graduation_year=getGrad(pdata['grade']), section=pdata['section'],
                code=pdata['code'], medium=pdata['medium'], shift=pdata['shift'],
                form_teacher=pdata['form_teacher'])
            account.save()
            messages.success(
                request, "Your account has been successfully created. You can now log in.")
            return redirect('login')
            # add a message saying ur account has been created
            # redirect to the login page
    else:
        uform = UserRegisterForm()
        pform = ProfileRegisterForm()

    context = {'uform': uform, 'pform': pform}
    return render(request, 'frontend/register.html', context)
