from django.contrib import admin
from .models import Phone

@admin.register(Phone)
class CarAdmin(admin.ModelAdmin):
    # list_display = ['id', 'brand', 'model', 'color', ]
    # list_filter = ['brand', 'model', ]
    pass



