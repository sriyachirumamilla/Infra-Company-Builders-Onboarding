from django.contrib import admin
from django.urls import path
from onboarding.views import ForgotPasswordView, HomeView
from onboarding.views import RegisterView, LoginView, DashboardView, user_logout, CompanyCreateView, BuilderCreateView, CompanyListView
from onboarding.views import CompanyMemberCreateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('logout/', user_logout, name='logout'),
    path('companies/add/', CompanyCreateView.as_view(), name='company-add'),
    path('builders/add/', BuilderCreateView.as_view(), name='builder-add'),
    path('company_member/add/', CompanyMemberCreateView.as_view(), name='company-member-add'),
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot_password'),
]
