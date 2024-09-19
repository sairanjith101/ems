from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile/', views.profile_info, name='profile_info'),
    path('employees/', views.employees_page, name='employees'),
    path('help/', views.help_page, name='help'),
    path('leave/', views.leave_request, name='leave_page'),
    path('head_officers/', views.head_officers, name='head_officers'),
    path('attendance/', views.attendance_page, name='attendance'),
    path('logout/', views.logout_view, name='logout'),
    # path('login/', views.login_view, name='login'),
    # path('admin_view/', views.admin_view, name='admin_view'),
    # path('accounts/login/', views.login_view, name='login'), 
]