# Create your models here.
from django.db import models

# Create your models here.

# First make sure that you have kept your app which is expensetrackerapp in the "INSTALLEDAPPS",after that
# you have to makemigrations and the migrate,and also make sure that you register your app in the admin.py section!


class Expenses(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    savingexp = models.CharField(max_length=50)
    date = models.CharField(max_length=20)
    month = models.CharField(max_length=100)
    expensegain = models.CharField(max_length=100)
    value = models.CharField(max_length=20)

    def __repr__(self):
        return f'{self.sno} {self.name},{self.savingexp},{self.date},{self.month},{self.expensegain},{self.value}'


class Todo(models.Model):

    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=20)
    month = models.CharField(max_length=100)
    value = models.CharField(max_length=250)

    def __repr__(self):
        return f'{self.sno} {self.name},{self.date},{self.month},{self.value}'


class CreateUser(models.Model):
    sno = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __repr__(self):
        return f' {self.sno},{self.fullname},{self.username},{self.password}'
