from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    profile_picture = forms.ImageField(required=False)  # Add the profile_picture field

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    # Override save method to handle profile creation and image saving
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        if 'profile_picture' in self.cleaned_data:
            profile_picture = self.cleaned_data['profile_picture']
            # Create UserProfile for the newly created user
            user_profile = UserProfile.objects.create(user=user, profile_picture=profile_picture)
            user_profile.save()
        return user
