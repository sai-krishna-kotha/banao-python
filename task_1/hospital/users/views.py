from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Account created successfully. Please login.")
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.user_type == user_type:
                    login(request, user)
                    if user_type == 'patient':
                        return redirect('patient_dashboard')
                    elif user_type == 'doctor':
                        return redirect('doctor_dashboard')
                else:
                    messages.error(request, "Selected role does not match your account role.")
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('login')

@login_required
def patient_dashboard(request):
    return render(request, 'users/dashboard.html', {'user': request.user})

@login_required
def doctor_dashboard(request):
    return render(request, 'users/dashboard.html', {'user': request.user})
