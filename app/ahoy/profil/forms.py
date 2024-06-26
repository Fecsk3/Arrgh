from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm as DjangoPasswordChangeForm

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

from django import forms
from django.contrib.auth.forms import PasswordChangeForm as DjangoPasswordChangeForm
from django.contrib.auth.models import User

class CustomPasswordChangeForm(DjangoPasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        
        self.fields['new_password1'] = forms.CharField(
            widget=forms.PasswordInput(attrs={'class': 'custom-input', 'placeholder': 'New Password'}),
            help_text="",
            label="Új jelszó"
        )
        self.fields['new_password2'] = forms.CharField(
            widget=forms.PasswordInput(attrs={'class': 'custom-input', 'placeholder': 'Confirm New Password'}),
            help_text="",
            label="Új jelszó mégegyszer"
        )

        self.fields['old_password'] = forms.CharField(
            widget=forms.PasswordInput(attrs={'class': 'custom-input', 'placeholder': 'Old Password'}),
            help_text="",
            label="Régi jelszó"
        )

    class Meta:
        model = User
        fields = (
            "old_password",
            "new_password1",
            "new_password2",
        )


# class CustomPasswordChangeForm(DjangoPasswordChangeForm):
#     class Meta:
#         model = User
#         fields = (
#             "old_password",
#             "new_password1",
#             "new_password2",
#         )
#         widgets = {
#             'old_password': forms.PasswordInput(attrs={'class': 'custom-password-change-form'}),
#             'new_password1': forms.PasswordInput(attrs={'class': 'custom-password-change-form'}),
#             'new_password2': forms.PasswordInput(attrs={'class': 'custom-password-change-form'}),
#         }

