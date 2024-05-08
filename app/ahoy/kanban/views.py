from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Board, Column, Card
from django.contrib import messages

def kanban(request):
    boards = Board.objects.prefetch_related('columns__cards').all()
    return render(request, 'kanban.html', {'boards': boards})

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
    

def generate_trello_cards(session_data):
    try:
        return generate_card_from_functional_specs(session_data)
    
    except Exception as e:
        print(f"Error generating Trello cards: {e}")
        return False
    
def create_board_and_coloumns(session_data, team_id):
    try:
        form_data = session_data.get('form_data', '')
        project_title = form_data.get('title', '')

        new_board = Board.objects.create(
            title=project_title,
            created_by=team_id,
        )

        column_titles = ['To Do', 'In Progress', 'Review', 'Testing', 'Done']
        for index, column_title in enumerate(column_titles):
            new_column = Column.objects.create(
                title=column_title,
                board=new_board,
                order=index
            )

        return True, new_board

    except Exception as e:
        print(f"Error creating board with columns: {e}")
        return False, None
    
def generate_card_from_functional_specs(session_data):
    try:
        team_id = session_data['selected_team_id']
        functional_specification = session_data.get('functional_specification', '')
        prompt = "Make Trello Cards (title, description) from this document:\n" + functional_specification + "\n structured as title and description separated by a newline"
        response = generate_gpt_response(prompt)

        success, board = create_board_and_coloumns(session_data, team_id)
        if not success:
            return False

        first_column = board.columns.first()

        card_data_list = response.split('\n\n') 

        max_order = first_column.cards.aggregate(Max('order'))['order__max'] or 0

        for card_data in card_data_list:
            title, description = card_data.split('\n', 1)

            new_card = Card.objects.create(
                title=title.strip(),
                description=description.strip(),
                column=first_column,
                order = max_order + 1,
            )

        return True

    except Exception as e:
        print(f"Error generating Trello card from functional specs: {e}")
        return False