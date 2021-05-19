from django.contrib import admin


from expensetrackerapp.models import Expenses, Todo, CreateUser

# Register your models here.


admin.site.register(Expenses)

admin.site.register(Todo)

admin.site.register(CreateUser)
