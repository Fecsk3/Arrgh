from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Board, Column, Card

def kanban(request):
    boards = Board.objects.prefetch_related('columns__cards').all()
    return render(request, 'kanban.html', {'boards': boards})

def board_detail(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'board_detail.html', {'board': board})

def create_card(request, column_id):
    if request.method == 'POST':
        column = get_object_or_404(Column, pk=column_id)
        title = request.POST.get('title')
        description = request.POST.get('description')
        order = column.cards.count()
        card = Card.objects.create(title=title, description=description, column=column, order=order)
        return JsonResponse({'status': 'success', 'card_id': card.id})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed.'})

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
