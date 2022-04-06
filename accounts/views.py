from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib import messages
from transactions.models import Balance
from .forms import SigninForm, SignupForm

# Create your views here.


@login_required
def home(request):
    return render(request, 'accounts/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=form.cleaned_data.get('username'))
            group = Group.objects.get(name='Users')
            user.groups.add(group,)
            Balance.objects.create(user=user).save()
            return HttpResponseRedirect(reverse('accounts:signin'))
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('accounts:home')
                messages.error(request, 'Password is wrong.', 'danger')

            except User.DoesNotExist:
                messages.error(request, 'No such user', 'danger')
    else:
        messages.warning(request, 'You must sign in to continue!', 'warning')
        form = SigninForm()
    return render(request, 'accounts/signin.html', {'form': form})


def signout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('accounts:home')
