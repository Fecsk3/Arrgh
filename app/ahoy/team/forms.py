from django import forms
from index.models import Team, TeamMember
from django.contrib.auth.models import User

class SeniorSelectionForm(forms.Form):
    senior = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True), label="Senior")

class TeamCreationForm(forms.Form):
    selected_users = forms.ModelMultipleChoiceField(
        queryset=None,
        label="Kit szeretne a csapatba belerakni?",
        widget=forms.CheckboxSelectMultiple,
        required=False  # Nem kötelező kitölteni, mert lehet, hogy nincs elérhető felhasználó
    )

    def __init__(self, *args, **kwargs):
        super(TeamCreationForm, self).__init__(*args, **kwargs)
        self.fields['selected_users'].queryset = self.get_available_users()

    def get_available_users(self):
        # Szűrjük azokat a felhasználókat, akik nem is_staff, nem is_superuser és nincsenek a TeamMemberben
        return User.objects.filter(is_staff=False, is_superuser=False).exclude(
            id__in=TeamMember.objects.values_list('user_id', flat=True)
        )

    def clean_selected_users(self):
        selected_users = self.cleaned_data.get('selected_users', [])
        if len(selected_users) == 0:
            raise forms.ValidationError("Legalább egy felhasználót ki kell választani!")

        if len(selected_users) > 4:
            raise forms.ValidationError("Maximum négy felhasználót lehet kiválasztani!")

        return selected_users