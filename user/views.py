from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from .forms import registerUserForm, profileForm, userUpdateForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = registerUserForm(request.POST)
        if form.is_valid():
            profile = form.save()
            user_profile = UserProfile(user=profile)
            user_profile.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            if user is not None:
                login(request, user)
                messages.success(request, f'sucessfully created {username}')
                return redirect('home')
        else:
                messages.success(request, f'error')
                return redirect(register)
            
    else:
        form = registerUserForm()
        data = {
            'form': form
        }
        return render(request, 'user/register.html', data)



def login_user(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'sucessfully loged in {username}')
                return redirect('home')
    else:
        return render(request, 'user/login.html')



def logout_user(request):
    logout(request)
    messages.success(request, "You've been logged out")
    return redirect('home')


def profile(request):

    if request.method == 'POST':
        p_form = profileForm(request.POST, request.FILES, instance=request.user.userprofile )
        u_form = userUpdateForm(request.POST, instance=request.user)
        
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()

            messages.success(request, 'your account has been updated')
            return redirect(profile)
        else:
            messages.success(request, 'an error has occured')
            return redirect(profile)

    else:

        p_form = profileForm(instance=request.user.userprofile )
        u_form = userUpdateForm(instance=request.user)
        data = {
            'p_form':p_form,
            'u_form':u_form,
        }

    return render(request, 'user/profile.html', data)