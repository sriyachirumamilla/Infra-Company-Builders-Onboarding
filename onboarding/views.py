from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistrationForm, BuilderForm, CompanyForm
from .models import Company, Builder
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User

# Home View
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

# Register View
class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')

            if password != confirm_password:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'register.html', {'form': form})

            if User.objects.filter(username=email).exists():
                messages.error(request, 'A user with this email already exists. Please log in or use a different email.')
                return render(request, 'register.html', {'form': form})

            User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')  # Redirect to login page after successful registration
        else:
            messages.error(request, 'There was an error with your submission. Please correct the errors below.')

        return render(request, 'register.html', {'form': form})


# Login View
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Ensure 'dashboard' is the correct URL name
            else:
                messages.error(request, 'Invalid email or password.')
        return render(request, 'login.html', {'form': form})

from django.shortcuts import render, redirect
from django.views import View
from .forms import CompanyForm, BuilderForm, CompanyMemberForm
from .models import Company, Builder, CompanyMember

class CompanyMemberCreateView(View):
    def get(self, request):
        form = CompanyMemberForm()
        return render(request, 'company_member_form.html', {'form': form})

    def post(self, request):
        form = CompanyMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company-list')  # Redirect to company list or appropriate page after association
        return render(request, 'company_member_form.html', {'form': form})


# Dashboard View
class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        company_member_form = CompanyMemberForm()  # Assuming you've created a form for CompanyMember
        context = {
            'company_member_form': company_member_form,
        }
        return render(request, 'dashboard.html', context)



# Logout View
def user_logout(request):
    logout(request)
    return redirect('login')

# Company Create View
class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company_form.html'
    success_url = '/companies/'

# Builder Create View
class BuilderCreateView(CreateView):
    model = Builder
    form_class = BuilderForm
    template_name = 'builder_form.html'
    success_url = '/companies/'

# Company List View
class CompanyListView(ListView):
    model = Company
    template_name = 'company_list.html'

# Forgot Password View
class ForgotPasswordView(View):
    def get(self, request):
        return render(request, 'forgot_password.html')
