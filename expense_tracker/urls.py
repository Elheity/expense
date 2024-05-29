"""
URL configuration for expense_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from expenses import views as expense_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', expense_views.register, name='register'),
    path('login/', expense_views.login_view, name='login'),
    path('logout/', expense_views.logout_view, name='logout'),
    path('add_expense/', expense_views.add_expense, name='add_expense'),
    path('expense_list/', expense_views.expense_list, name='expense_list'),
    path('', expense_views.expense_list, name='home'),
]