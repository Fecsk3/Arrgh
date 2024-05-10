from django import forms
from django.contrib.auth.models import User

class SendMessageForm(forms.Form):
    # Kiszűrjük az is_staff felhasználókat
    staff_users = User.objects.filter(is_staff=True)
    
    # Létrehozunk egy listát a felhasználók felhasználóneveivel
    user_choices = [(user.id, user.username) for user in staff_users]
    
    # Hozzáadjuk az "Mindenki" opciót
    user_choices.insert(0, (0, 'Mindenki'))
    
    # Definiáljuk a to_user mezőt a létrehozott választékkal
    to_user = forms.ChoiceField(choices=user_choices, initial=0)
    title = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(SendMessageForm, self).__init__(*args, **kwargs)
        # Alkalmazzuk az üres választék kezelését
        self.fields['to_user'].empty_label = None
