from django.contrib import admin
from .models import Attraction

@admin.register(Attraction)
class AttractionsAdmin(admin.ModelAdmin):
    ...
