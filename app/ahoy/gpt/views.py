from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from freeGPT.Client.gpt4 import Completion

@login_required(redirect_field_name="bejelentkezes_szukseges")
def gpt(request):
    if request.method == 'POST':
        prompt = request.POST.get('input')
        try:
            completion_generator = Completion()
            response = completion_generator.create(prompt)
            return render(request, 'gpt.html', {'response': response})
        except Exception as e:
            error_message = f"Error: {e}"
            return render(request, 'gpt.html', {'error_message': error_message})
    else:
        return render(request, 'gpt.html')