from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Board, Title, Task

@login_required(redirect_field_name="bejelentkezes_szukseges")
def kanban(request):
    # message = request.GET.get('message', None) 

    boards = Board.objects.prefetch_related('titles__tasks').all()
    
    context = {
        'boards': boards
    }           

    return render(request, 'kanban.html', context)
    if (message):
        return render(request, 'kanban.html', {'message': message})
    else:
        return render(request, 'kanban.html')