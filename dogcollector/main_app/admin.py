from django.contrib import admin

# Register your models here.
from .models import Dog, Feeding, Toy


# allow crud updates for out Dog table in our admin app
admin.site.register(Dog)
admin.site.register(Feeding)
admin.site.register(Toy)
