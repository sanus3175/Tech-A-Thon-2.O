from msilib.schema import Class
from django.contrib import admin
from .models import (
Bloger,
Blog,

)

@admin.register(Bloger)
class BlogerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'address', 'city', 'pincode', 'state', 'email', 'contact_no']

@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',  'description', 'category', 'blog_image']
