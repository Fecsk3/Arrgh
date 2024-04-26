from django import forms
from django.contrib.auth.models import User
from index.models import TeamMember

class TeamCreationForm(forms.Form):
    senior = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True),
                                    label='Senior')
    members = forms.ModelMultipleChoiceField(queryset=User.objects.filter(is_staff=False, is_superuser=False)
                                             .exclude(id__in=TeamMember.objects.values_list('user_id', flat=True)),
                                             label='Csapattagok',
                                             widget=forms.SelectMultiple(attrs={'size': 3}))

""" from django import forms
from django.contrib.auth.models import User
from index.models import TeamMember, Team


class TeamCreationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TeamCreationForm, self).__init__(*args, **kwargs)
        self.fields['senior'] = forms.ModelChoiceField(
            queryset=User.objects.filter(is_staff=True),
            label='Senior'
        )

    def clean_members(self):
        members = self.cleaned_data['members']
        if len(members) < 1:
            raise forms.ValidationError("Legalább 1 csapattagot válasszon ki.")
        elif len(members) > 5:
            raise forms.ValidationError("Maximum 5 csapattagot válasszon ki.")
        return members

    def save(self):
        senior = self.cleaned_data['senior']
        team = Team.objects.create(senior=senior)
        members = self.cleaned_data['members']
        for member in members:
            TeamMember.objects.create(user=member, team=team)


class AddMembersForm(forms.Form):
    members = forms.ModelMultipleChoiceField(
        queryset=None,
        label='Válasszon csapattagokat',
        widget=forms.CheckboxSelectMultiple()
    )

    def __init__(self, *args, **kwargs):
        team_id = kwargs.pop('team_id')
        super(AddMembersForm, self).__init__(*args, **kwargs)
        
        # Lekérdezi azokat az id-kat, amelyek valamelyik csapatban szerepelnek
        existing_member_ids = TeamMember.objects.values_list('user_id', flat=True)
        
        # Szűri a felhasználókat, kizárva azokat, akik bármely csapatban szerepelnek
        self.fields['members'].queryset = User.objects.filter(
            is_staff=False,
            is_superuser=False
        ).exclude(
            id__in=existing_member_ids
        )
 """