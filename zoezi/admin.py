from django.contrib import admin
from .models import PORTFOLIOITEM


# Register your models here.
class PORTFOLIOITEMAdmin(admin.ModelAdmin):
    list_display = "title", "subtitle", "Description"


admin.site.register(PORTFOLIOITEM),
