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
