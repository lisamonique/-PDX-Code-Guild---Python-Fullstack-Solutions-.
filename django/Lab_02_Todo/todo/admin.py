from django.contrib import admin
from .models import Priority, TodoItem

# Register your models here.

admin.site.register(TodoItem)
admin.site.register(Priority)
