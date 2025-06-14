from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.login_view, name='login'),
    path('signout/', views.signout, name='signout'),
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
]
