from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from freeGPT import AsyncClient
from asyncio import run

@login_required(redirect_field_name="bejelentkezes_szukseges")
def gpt(request):
    message = request.GET.get('message', None) 
    response = ""

    if request.method == 'POST':
        input_text = request.POST.get('input', '')
        if input_text:
            response = generate_gpt_response(input_text)

    if message:
        return render(request, 'gpt.html', {'message': message, 'response': response})
    else:
        return render(request, 'gpt.html', {'response': response}) 

async def generate_gpt_response(input_text):
    try:
        gpt_instance = AsyncClient()
        response = await gpt_instance.create_completion("MODEL", input_text)
        return response
    except Exception as e:
        return str(e)
