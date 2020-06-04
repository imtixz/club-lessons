from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from backend.models import Profile


class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['fname', 'lname', 'number', 'gender',
                  'address', 'ssc_year', 'medium', 'shift', 'section', 'code', 'form_teacher']
        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'number': 'Phone Number',
            'address': 'Address',
            'gender': 'Gender',
            'ssc_year': 'SSC Year',
            'section': 'Section',
            'code': 'Code No.',
            'medium': 'Medium',
            'shift': 'Shift',
            'form_teacher': 'Form Teacher'

        }
        help_texts = {
            'number': 'Enter a phone number we can use to contact you',
            'address': "Enter your address. If you don't want to give your full address for some reason, giving a general vicinity is also okay (e.g. sector 11, uttara)",
            'ssc_year': "Enter the year you will give ssc or have given ssc. This will be used to dynamically determine which grade you're in right now.",
            'section': "Enter which section you're in (in Rajuk)",
            'code': "Enter your normal code number (from Rajuk)",
            'form_teacher': "Enter the full name or abbreviation of your form teacher"
        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username',
                  'email', 'password1', 'password2']
        help_texts = {
            'username': "You will use this username to log in to the website. Use 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        }


class loginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(
        max_length=32, widget=forms.PasswordInput, label="Password")
    rcdc_password = forms.CharField(max_length=32, widget=forms.PasswordInput,
                                    label="RCDC Password", help_text="Enter the secret rcdc password. If you don't know the rcdc password, ask someone else from the club.")
