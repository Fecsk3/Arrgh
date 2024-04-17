from pathlib import Path
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from freeGPT.Client.gpt3 import Completion
from .forms import ProjectForm

@login_required(redirect_field_name="bejelentkezes_szukseges")
def gpt(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return render(request, 'gpt.html', {'project': project})
    else:
        form = ProjectForm()
    return render(request, 'gpt.html', {'form': form})
    # prompt = "django project"
    # gpt_response = generate_gpt_response(prompt)
    # print(gpt_response)
    # templates_content = load_templates()
    # template_response_kovspec = generate_response_for_template(templates_content[0], gpt_response)
    # print(template_response_kovspec)
    # template_response_funkcpec = generate_response_for_template(templates_content[1], template_response_kovspec)
    # template_response_rendszerterv = generate_response_for_template(templates_content[2], template_response_funkcpec)

    # template_responses = [template_response_kovspec, template_response_funkcpec, template_response_rendszerterv]
    # print(template_responses)
    # save_templates_responses(template_responses)

    # if request.method == 'POST':
    #     prompt = request.POST.get('input')
    #     try:
    #         # generate_response_for_templates(load_templates(), generate_gpt_response(prompt))
    #         return render(request, 'gpt.html')
    #     except Exception as e:
    #         error_message = f"Error: {e}"
    #         return render(request, 'gpt.html', {'error_message': error_message})
    # else:
    return render(request, 'gpt.html')

def generate_gpt_response(prompt):
    completion_generator = Completion()
    response = completion_generator.create(prompt)
    return response

def load_templates():
    templates_dir = Path(settings.BASE_DIR) / 'static' / 'docs'

    template_filenames = [
        'kovetelmeny_specifikacio.md',
        'funkcionalis_specifikacio.md',
        'rendszerterv.md'
    ]

    template_files = [templates_dir / filename for filename in template_filenames]

    templates_content = []
    for template_file in template_files:
        with open(template_file, 'r') as f:
            template_content = f.read()
            templates_content.append(template_content)

    print(templates_content[0])
    return templates_content

# def generate_response_for_templates(templates_content, gpt_response):
#     template_responses = []
#     for template_content in templates_content:
#         template_prompt = gpt_response + template_content
#         template_response = generate_gpt_response(template_prompt)
#         template_responses.append(template_response)
#     return template_responses

def generate_response_for_template(template_content, gpt_response):
    template_prompt = gpt_response + template_content
    template_response = generate_gpt_response(template_prompt)
    return template_response

def save_templates_responses(template_responses):
    saved_files = []
    media_root = Path(settings.MEDIA_ROOT)
    output_dir = media_root / 'user_generated_docs'
    
    template_filenames = [
        'kovetelmeny_specifikacio_generated.md',
        'funkcionalis_specifikacio_generated.md',
        'rendszerterv_generated.md'
    ]

    for filename, response in zip(template_filenames, template_responses):
        file_path = output_dir / filename
        with open(file_path, 'w') as file:
            file.write(response)
        saved_files.append(file_path)
    
    return saved_files