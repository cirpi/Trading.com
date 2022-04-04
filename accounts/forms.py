from platform import mac_ver
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm



class SignupForm(UserCreationForm):
    def __init__(self, *args,  **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'autofocus':False, 'class':'my-1',}
        self.fields['password2'].label = 'Confirm Password'
        self.fields['email'].widget.attrs = {'class':'validate my-1', 'required':'',}
        self.fields['email'].unique = True
        self.fields['first_name'].widget.attrs = { 'required':'', 'autofocus':True}
        self.fields['last_name'].widget.attrs = { 'required':''} 
        self.fields['password1'].widget.attrs = { 'required':'',}
        self.fields['password2'].widget.attrs = { 'required':'',}

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        users = User.objects.filter(email=email)
        if len(users) > 0:
            raise forms.ValidationError('Email already exists.')
        if not email:
            raise forms.ValidationError('Email must not be empty.')
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError('Firstname must not be empty.')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError('Firstname must not be empty.')
        return last_name



class SigninForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'my-3', 'required':''}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class':'my-3', 'required':''}))