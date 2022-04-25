from django.contrib import admin

# Register your models here.
from .models import Dog


# allow crud updates for out Dog table in our admin app
admin.site.register(Dog)
