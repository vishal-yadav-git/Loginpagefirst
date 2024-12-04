from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')  # Show user and profile picture in the list
    search_fields = ('user__username',)  # Allow searching by username

admin.site.register(UserProfile, UserProfileAdmin)  # Register the UserProfile model with customized admin
