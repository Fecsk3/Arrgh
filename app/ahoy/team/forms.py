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
