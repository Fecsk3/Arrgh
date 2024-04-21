from django import forms
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):

    username = forms.CharField(
        max_length=150,
        help_text="",
        label="Felhasználónév",
        
    )
    first_name = forms.CharField(
        label="Keresztnév",
    )
    last_name = forms.CharField(
        label="Vezetéknév",
    )
    email = forms.EmailField(
        max_length=254,
        help_text="",
        label="Email-cím",
    )

    class Meta:
            model = User
            fields = (
                "username",
                "first_name",
                "last_name",
                "email",
            )
