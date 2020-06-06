from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from backend.models import Profile


class ProfileRegisterForm(forms.Form):
    fname = forms.CharField(max_length=255, label='First Name')
    lname = forms.CharField(max_length=255, label="Last Name")
    number = forms.CharField(max_length=32, label="Phone Number",
                             help_text="Enter a phone number we can use to contact you")
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('O', 'Others'))
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

    GRADE_CHOICES = (('6', 'Class 6'), ('7', 'Class 7'),
                     ('8', 'Class 8'), ('9', 'Class 9'), ('10', 'Class 10'),
                     ('SSC Candidate', 'SSC Candidate'), ('11', 'Class 11'),
                     ('12', 'Class 12'), ('HSC Candidate', 'HSC Candidate'), ('Alumni', 'Alumni'))
    grade = forms.ChoiceField(choices=GRADE_CHOICES)
    MEDIUM_CHOICES = (('E', 'English'), ('B', 'Bangla'))
    medium = forms.ChoiceField(choices=MEDIUM_CHOICES)
    SHIFT_CHOICES = (('M', 'Morning'), ('D', 'Day'))
    shift = forms.ChoiceField(choices=SHIFT_CHOICES)
    section = forms.CharField(max_length=32)
    code = forms.CharField(max_length=16)
    form_teacher = forms.CharField(
        max_length=32, help_text="Enter the full name or abbreviation of your form teacher")
    address = forms.CharField(
        max_length=1024, help_text="Enter your address. If you don't want to give your full address for some reason, giving a general vicinity is also okay (e.g. sector 11, uttara)")


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
