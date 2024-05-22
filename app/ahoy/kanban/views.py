from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Board, Column, Card
from django.contrib import messages
from freeGPT.Client.gpt3 import Completion
from django.db.models import Max
from index.models import Team, TeamMember
from pathlib import Path
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required()
def kanban(request):
    user_id = User.objects.get(id=request.user.id) 
    is_senior = Team.objects.filter(senior_id=user_id).exists()
    senior_teams = None
    boards = None

    if is_senior:
        senior_teams = Team.objects.filter(senior_id=user_id)
        selected_team_id = None

        if request.method == 'POST' and 'generate_board' in request.POST:
            selected_team_id = int(request.POST.get('selected_team'))

            if Board.objects.filter(created_by_id=selected_team_id).exists():
                messages.info(request, 'This team already has a board.')
            else:
                success, new_board = create_board_and_columns(selected_team_id)
                if success:
                    messages.success(request, 'The board was created successfully.')
                else:
                    messages.error(request, 'An error occurred while creating the board.')  

            if selected_team_id:
                boards = Board.objects.filter(created_by_id=selected_team_id)

        if not boards:
            boards = Board.objects.filter(created_by__in=senior_teams)
        
        return render(request, 'kanban.html', {'senior_teams': senior_teams, 'is_senior': is_senior, 'boards': boards})
    else:
        boards = Board.objects.prefetch_related('columns__cards').all()
        return render(request, 'kanban.html', {'boards': boards})

def get_user_team_id(user_id):
    try:
        team_member = TeamMember.objects.get(user_id=user_id)
        return team_member.team_id
    except TeamMember.DoesNotExist:
        try:
            team = Team.objects.get(senior_id=user_id)
            return team.teams_id
        except Team.DoesNotExist:
            return None

def create_card(request, column_id):
    if request.method == 'POST':
        column = get_object_or_404(Column, pk=column_id)
        title = request.POST.get('title')
        description = request.POST.get('description')
        order = column.cards.count()
        try:
            card = Card.objects.create(title=title, description=description, column=column, order=order)
            messages.success(request, 'Card created successfully.')
            return redirect('kanban')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return redirect('kanban')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('kanban')

def move_card(request, card_id, column_id):
    if request.method == 'POST':
        card = get_object_or_404(Card, pk=card_id)
        new_column = get_object_or_404(Column, pk=column_id)
        old_column = card.column
        card.column = new_column
        card.order = new_column.cards.count()
        card.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed.'})

def remove_card(request, card_id):
    if request.method == 'POST':
        card = get_object_or_404(Card, pk=card_id)
        try:
            card.delete()
            messages.success(request, 'Card deleted successfully.')
            return redirect('kanban')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return redirect('kanban')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('kanban')
    
def edit_card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        color = request.POST.get('color')
        
        print(f"Received title: {title}, description: {description}, color: {color}")

        if title and description:
            try:
                card.title = title
                card.description = description
                card.color = color
                card.save()
                messages.success(request, 'Card updated successfully.')
                return redirect('kanban')
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
                return redirect('kanban')
        else:
            messages.error(request, 'Title and description cannot be empty.')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('kanban')

def get_card_color(request, card_id):
    try:
        card = Card.objects.get(id=card_id)
        color = card.color
        return JsonResponse({'color': color})
    except Card.DoesNotExist:
        return JsonResponse({'error': 'Card does not exist'}, status=404)


def load_team_docs(team_id):
    team = Team.objects.get(teams_id=team_id)
    directory = team.directory

    if directory:
        docs_dir = Path(settings.BASE_DIR) / 'media' / 'user_generated_docs' / directory

        docs_filenames = [
            'requirements_specification_generated.md',
            'functional_specification_generated.md',
            'system_plan_generated.md'
        ]

        docs_files = [docs_dir / filename for filename in docs_filenames]

        docs_content = []
        for docs_file in docs_files:
            with open(docs_file, 'r') as f:
                doc_content = f.read()
                docs_content.append(doc_content)
        return docs_content
    else:
        messages.error("Create documentation for project first")

def generate_gpt_response(prompt):
    completion_generator = Completion()
    response = completion_generator.create(prompt)
    return response

def generate_trello_cards(session_data):
    try:
        return generate_card_from_choosed_specs(session_data)
    
    except Exception as e:
        print(f"Error generating Trello cards: {e}")
        return False
    
def create_board_and_columns(team_id):
    try:
        team = Team.objects.get(teams_id=team_id)
        project_title = team.project_title

        new_board = None

        if project_title:
            new_board = Board.objects.create(
                title=project_title,
                created_by=team,
            )
        else:
            print("Create documentation for project first")
            return False, None

        if (new_board):
            column_titles = ['To Do', 'In Progress', 'Review', 'Testing', 'Done']
            for index, column_title in enumerate(column_titles):
                new_column = Column.objects.create(
                    title=column_title,
                    board=new_board,
                    order=index
                )
                if new_column is None:
                    print(f"Failed to create column '{column_title}'. Rolling back board creation.")
                    new_board.delete()
                    return False, None
        else:
            print("Failed to create board.")
            return False, None
        
        if (new_board and new_column):
            return True, new_board

    except Exception as e:
        print(f"Error creating board with columns: {e}")
        return False, None
    
def generate_card_from_choosed_specs(session_data):
    try:
        team_id = session_data.get('selected_team_id')
        functional_specification = session_data.get('functional_specification', '')

        if not team_id:
            print("No team selected.")
            return False

        if not functional_specification:
            print("No functional specification provided.")
            return False

        prompt = "Make Trello Cards (title, description) from this document:\n" + functional_specification + "\n structured as title and description separated by a newline"
        response = generate_gpt_response(prompt)

        if not response:
            print("No response from GPT.")
            return False

        success, new_board = create_board_and_columns(team_id)
        if not success:
            print("Failed to create board and columns.")
            return False

        first_column = new_board.columns.first()

        card_data_list = response.split('\n\n')

        max_order = first_column.cards.aggregate(Max('order'))['order__max'] or 0

        for card_data in card_data_list:
            title, description = card_data.split('\n', 1)

            new_card = Card.objects.create(
                title=title.strip(),
                description=description.strip(),
                column=first_column,
                order=max_order + 1,
            )

        print("Trello cards generated successfully.")
        return True

    except Exception as e:
        print(f"Error generating Trello card from functional specs: {e}")
        return False
