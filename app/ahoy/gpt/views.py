
import logging
from pathlib import Path
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from freeGPT.Client.gpt3 import Completion
from .forms import ProjectForm
from django.contrib import messages
import markdown2
from django.utils.html import escape

logger = logging.getLogger(__name__)

@login_required()
def gpt(request):
    form = ProjectForm()
    form_submitted = False
    
    def render_template_with_data(template_name, data):
        data.update({'form': form, 'form_submitted': form_submitted})
        return render(request, template_name, data)

    if request.method == 'POST':
        try:
            if 'project_specialization_form' in request.POST:
                form = ProjectForm(request.POST)
                if form.is_valid():
                    form_data = form.cleaned_data
                    request.session['form_data'] = form_data

                    prompt = description_for_project(form_data)
                    prompt = escape(prompt) 
                    project_description = generate_gpt_response(prompt)
                    request.session['project_description'] = project_description

                    templates = load_templates()
                    request.session['requirements_specification_template'] = templates[0]
                    request.session['functional_specification_template'] = templates[1]
                    request.session['system_plan_template'] = templates[2]

                    project_description = markdown2.markdown(project_description)
                    form_submitted = True
                    return render_template_with_data('gpt.html', {'project_description': project_description})
                else:
                    messages.error(request, "Invalid form data. Please check your inputs.")

            elif 'generate_requirements_specification_form' in request.POST:
                if 'project_description' in request.session:
                    try:
                        prompt = request.session['project_description'] + request.session['requirements_specification_template']
                        requirements_specification = generate_gpt_response(prompt)
                        request.session['requirements_specification'] = requirements_specification
                        requirements_specification = markdown2.markdown(requirements_specification)
                        form_submitted = True
                        return render_template_with_data('gpt.html', {'requirements_specification': requirements_specification})
                    except Exception as e:
                        messages.error(request, f"Error generating requirements specification: {e}")
                    
                else:
                    messages.error(request, "No project description found.")

            elif 'generate_functional_specification_form' in request.POST:
                if 'requirements_specification' in request.session:
                    try:
                        prompt = request.session['project_description'] + request.session['functional_specification_template']
                        request.session.pop('requirements_specification_template', None)
                        functional_specification = generate_gpt_response(prompt)
                        request.session['functional_specification'] = functional_specification
                        functional_specification = markdown2.markdown(functional_specification)
                        form_submitted = True
                        return render_template_with_data('gpt.html', {'functional_specification': functional_specification})
                    except Exception as e:
                        messages.error(request, f"Error generating functional specification: {e}")
                else:
                    messages.error(request, "No requirements specification found.")

            elif 'generate_system_plan_form' in request.POST:
                if 'functional_specification' in request.session:
                    try:
                        if 'form_data' in request.session:
                            prompt = request.session['project_description'] + request.session['system_plan_template']
                            request.session.pop('functional_specification_template', None)
                            system_plan = generate_gpt_response(prompt)
                            request.session['system_plan'] = system_plan
                            system_plan = markdown2.markdown(system_plan)
                            form_submitted = True
                            return render_template_with_data('gpt.html', {'system_plan': system_plan})
                    except Exception as e:
                        messages.error(request, f"Error generating system plan: {e}")
                else:
                    messages.error(request, "No functional specification found.")
            
            elif 'show_summary' in request.POST:
                if 'system_plan' in request.session:
                    try:
                        summary = f"Requirements Specification\n" \
                                    f"Functional Specification\n" \
                                    f"System Plan"
                        summary_lines = summary.split('\n')

                        form_submitted = True

                        return render_template_with_data('gpt.html', {'summary': summary_lines})

                    except Exception as e:
                        messages.error(request, f"Error showing summary: {e}")
                    finally:
                        request.session.pop('system_plan_template', None)

                else:
                    messages.error(request, "No system plan found.")

            elif 'save_documents' in request.POST:
                try:                        
                    template_responses = []
                    template_responses.append(request.session['requirements_specification'])
                    template_responses.append(request.session['functional_specification'])
                    template_responses.append(request.session['system_plan'])
                    successful_saving = save_templates_responses(template_responses)
                    if successful_saving:
                        messages.success(request, "Generated documents successfully saved.")
                    else:
                        messages.error(request, "Error saving generated documents.")
                except Exception as e:
                    messages.error(request, f"Error saving generated documents: {e}")
                finally:
                    request.session.pop('project_description', None)
            
            elif 'generate_trello_cards' in request.POST:
                try:
                    successful_generation = generate_trello_cards(request.session)
                    if successful_generation:
                        messages.success(request, "Trello cards generated successfully.")
                    else:
                        messages.error(request, "Error generating Trello cards.")
                except Exception as e:
                    messages.error(request, f"Error generating Trello cards: {e}")
                finally:
                    request.session.pop('form_data', None)
                    request.session.pop('requirements_specification', None)
                    request.session.pop('functional_specification', None)
                    request.session.pop('system_plan', None)
        
        except Exception as e:
            error_message = f"An unexpected error occurred: {e}"
            logger.error(error_message, exc_info=True, extra={'request': request})
            messages.error(request, error_message)

    else:
        form = ProjectForm()

    return render_template_with_data('gpt.html', {})

def generate_gpt_response(prompt):
    completion_generator = Completion()
    response = completion_generator.create(prompt)
    return response

def description_for_project(form_data):
    description = f"+ **Project Title:** {form_data.get('title')}\n"
    description += f"+ **Project Goal:** {form_data.get('goal')}\n"
    description += f"+ **Target Users:** {form_data.get('target_users')}\n"
    description += f"+ **Problem motivation:** {form_data.get('problem_motivation')}\n"
    description += "+ **Key Features:**\n"
    key_features = form_data.get('key_features', '').split('\n')
    for i, feature in enumerate(key_features, start=1):
        description += f"   + {feature.strip()}\n"
    description += f"+ **Technical Stack:** {form_data.get('technical_stack')}\n"  
    description += f"+ **Deliverables:** {form_data.get('deliverables')}\n"
    description += f"+ **Project Timeline:** {form_data.get('timeline')}\n"
    description += f"+ **Additional Information:** {form_data.get('additional_info')}\n"
    return description
  
def load_templates():
    templates_dir = Path(settings.BASE_DIR) / 'static' / 'docs'

    template_filenames = [
        'requirements_specification.md',
        'functional_specification.md',
        'system_plan.md'
    ]

    template_files = [templates_dir / filename for filename in template_filenames]

    templates_content = []
    for template_file in template_files:
        with open(template_file, 'r') as f:
            template_content = f.read()
            templates_content.append(template_content)
    return templates_content

def save_templates_responses(template_responses):
    saved_files = []
    media_root = Path(settings.MEDIA_ROOT)
    output_dir = media_root / 'user_generated_docs'
    
    template_filenames = [
        'requirements_specification_generated.md',
        'functional_specification_generated.md',
        'system_plan_generated.md'
    ]

    try:
        for filename, response in zip(template_filenames, template_responses):
            file_path = output_dir / filename
            with open(file_path, 'w') as file:
                file.write(response)
            saved_files.append(file_path)
        return True 
    
    except FileNotFoundError as e:
        logger.error(f"Error occurred while saving files: {e}")
        return False
    except PermissionError as e:
        logger.error(f"Permission error occurred while saving files: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error occurred while saving files: {e}")
        return False
    
def generate_trello_cards(session_data):
    try:
        form_data = session_data.get('form_data', '')
        title = form_data.get('title', '')

        requirements_specification = session_data.get('requirements_specification', '')
        functional_specification = session_data.get('functional_specification', '')
        system_plan = session_data.get('system_plan', '')

        #TODO: making trello cards in database
        
        return True
    
    except Exception as e:
        print(f"Error generating Trello cards: {e}")
        return False
