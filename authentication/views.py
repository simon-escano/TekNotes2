from django.shortcuts import render, redirect
from django.contrib.auth import logout as log_out
from .forms import RegisterForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            Profile.objects.create(user=user)

            return redirect('/auth/login/')
    else:
        form = RegisterForm()

    return render(request, 'authentication/register.html', {
        'form': form
    })

def logout(request):
    log_out(request)
    return redirect('/')