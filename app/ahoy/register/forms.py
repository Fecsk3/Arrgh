from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        help_text="",
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'username', 'class': 'form-control'})
    )
    first_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'first_name', 'class': 'form-control'})
    )
    last_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'last_name', 'class': 'form-control'})
    )
    email = forms.EmailField(
        label="",
        max_length=254,
        help_text="",
        widget=forms.EmailInput(attrs={'placeholder': 'mail@mail.com', 'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="",
        help_text="",
        widget=forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="",
        help_text="",
        widget=forms.PasswordInput(attrs={'placeholder': 'password again', 'class': 'form-control'})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ez az email cím már használatban van. Kérem, adjon meg másikat.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )