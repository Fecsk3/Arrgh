# forms.py

from django import forms
from index.models import Team

class TeamCreationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['senior']  # Itt jelöljük meg a mezőt, amit a form kezelni fog

    def __init__(self, *args, **kwargs):
        super(TeamCreationForm, self).__init__(*args, **kwargs)
        self.fields['senior'].label = "Senior"
