from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ImageUpdateForm, ForgetPasswordForm, ChangePasswordForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .Email import send_email
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account is created now you can login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        I_form = ImageUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and I_form.is_valid():
            u_form.save()
            I_form.save()
            messages.success(request, f'Your Account Info Is Updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        I_form = ImageUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form,
               'i_form': I_form
               }
    return render(request, 'users/profile.html', context)

def change_password(request, token):
    if request.method == 'POST':
        current_p = request.POST.get('current_p')
        new_p = request.POST.get('new_p')
        confirm_p = request.POST.get('confirm_p')
        print(current_p, new_p, confirm_p)
        token_obj = Profile.objects.filter(password_token = token).first()

    cp_form = ChangePasswordForm()
    context = {'CP_form': cp_form}
    return render(request, 'users/change_password.html', context)



import uuid
def forget_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if not User.objects.filter(username=username).first():
            messages.success(request, 'No User found with that user name')
            return redirect('forget-password')

        user_obj = User.objects.filter(username=username).first()
 gi       token = str(uuid.uuid4())
        token_obj = Profile.objects.get(user = user_obj)
        token_obj.password_token = token
        token_obj.save()
        send_email(user_obj.email, token)
        messages.success(request, f'An email has been send to your gmail, Check your inbox.')
        return redirect('forget-password')


    FP_form = ForgetPasswordFocdvd
    context = {'fp_form': FP_form}
    return render(request, 'users/forget_password.html', context)
