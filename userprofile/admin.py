from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Profile admin options
    """
    list_display = (
        'name',
        'gender',
        'age'
    )
    list_filter = ('gender', )
