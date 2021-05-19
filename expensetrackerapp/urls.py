"""expensetracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from expensetrackerapp import views

urlpatterns = [
    path('', views.login, name='login'),
    path('createaccount/', views.createaccount, name='createaccount'),
    path('createerror/', views.createerror, name='createerror'),
    path('home/', views.home, name='home'),
    path('addtodo/', views.addtodo, name='addtodo'),
    path('expenses/', views.expenses, name='expenses'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('transactions/', views.transactions, name='transactions'),
    path('displaytodo/', views.displaytodo, name='displaytodo'),
    path('error/', views.displaytodo, name='error'),
    path('dashboarderror/', views.dashboarderror, name='dashboarderror'),
    path('todoerror/', views.todoerror, name='todoerror'),
    path('exception/', views.exception, name='exception'),
    path('expenseerror/', views.expenseerror, name='expenseerror'),

]
