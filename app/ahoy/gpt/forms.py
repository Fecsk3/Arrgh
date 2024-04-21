from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '[Insert your project title here]'}),
            'goal': forms.Textarea(attrs={'placeholder': 'Develop a [Type of program] application that [Describe the main functionality of your program].'}),
            'target_users': forms.Textarea(attrs={'placeholder': 'This program is designed for [Who will use the program? (e.g., programmers, specific industry users)].'}),
            'problem_motivation': forms.Textarea(attrs={'placeholder': '[Explain the problem your program solves or the opportunity it addresses. Briefly mention any existing related projects (if applicable).]'}),
            'technical_stack': forms.Textarea(attrs={'placeholder': 'The project will utilize [List the programming languages, frameworks, or libraries you plan to use.].'}),
            'key_features': forms.Textarea(attrs={'placeholder': '[List 2-3 core functionalities of your program]\n[List 2-3 additional functionalities (optional)]'}),
            'deliverables': forms.Textarea(attrs={'placeholder': 'A fully functional program with a user interface (if applicable)\n[Mention any additional deliverables like documentation, test cases, etc.]'}),
            'timeline': forms.Textarea(attrs={'placeholder': '[Give a rough estimate of the project duration or any key milestones.]'}),
            'additional_info': forms.Textarea(attrs={'placeholder': '[Mention any specific technologies you\'re unsure about using or open to exploring.]\n[Indicate your desired tone for the description (e.g., concise, technical, user-centric)]'}),
        }