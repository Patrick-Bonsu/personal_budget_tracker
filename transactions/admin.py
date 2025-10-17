from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Transaction, Category

# Register your models here
admin.site.register(Transaction)
admin.site.register(Category)
