from django import forms
from .models import RegistrationData,loginData
class RegistrationForm(forms.Form):
    first_name=forms.CharField(
        label='Enter First Name',
        widget=forms.TextInput(
            attrs={
                'class':'from-control',
                'placeholder':'First Name'
            }
        )
    )
    last_name=forms.CharField(
        label='Enter Last Name',
        widget=forms.TextInput(
            attrs={
                'class':'from-control',
                'placeholder':'Last Name'
            }
        )
    )
    username=forms.CharField(
        label='Enter User Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'user Name'
            }
        )
    )
    password1=forms.CharField(
        label='Enter password1',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter password1'
            }
        )
    )
    email=forms.CharField(
        label='Enter Last Name',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email Id'
            }
        )
    )
    number=forms.CharField(
        label='Enter number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'mobile number'
            }
        )
    )
    dob=forms.CharField(
        label='Enter your date of birth',
        widget=forms.DateInput(
        attrs={
            'class':'form-control',
            'placeholder':'date of birth'
            }
        )
    )
    gender=forms.CharField(
        label='Enter your gender',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Gneder'
            }


        )
    )
class LoginForm(forms.Form):
    username=forms.CharField(
        label='Enter User Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-contrl',
                'placeholder':'Username'
            }
        )
    )
    password1=forms.CharField(
        label='Enter Your Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'password'
            }
        )
    )
