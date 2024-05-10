from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SendMessageForm
from index.models import Message, User

@login_required
def send_message(request):
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            to_user_id = form.cleaned_data['to_user']
            if to_user_id == 0:  # If "Mindenki" was selected
                to_user_id = 0  # Set to_user_id to 0
            title = form.cleaned_data['title']
            message_content = form.cleaned_data['message']

            # Create and save the message to the database
            Message.objects.create(
                from_user=request.user,
                to_user_id=to_user_id,
                title=title,
                message=message_content,
                read=False
            )
            return redirect('messages')  # Redirect to the messages list view
    else:
        form = SendMessageForm()

    return render(request, 'sendmessage.html', {'form': form})

@login_required
def superuser_messages_view(request):
    if request.method == 'GET':
        filter_type = request.GET.get('filter', 'unread')

        if filter_type == 'unread':
            # Szűrés az olvasatlan üzenetekre, de kizárva a to_user_id = 0 és read = 0 eseteket
            user_messages = Message.objects.filter(from_user=request.user, read=False).exclude(to_user_id=0)
        elif filter_type == 'read':
            user_messages = Message.objects.filter(from_user=request.user, read=True)
        elif filter_type == 'all':
            user_messages = Message.objects.filter(from_user=request.user, to_user_id=0)
        else:
            user_messages = None

        # Prepare message data for rendering in the template
        message_data = []
        for message in user_messages:
            if message.to_user_id == 0:
                to_user_name = "Mindenki"
            else:
                to_user = User.objects.filter(id=message.to_user_id).first()
                to_user_name = to_user.username if to_user else "Ismeretlen felhasználó"
            
            message_data.append({
                'to_user': to_user_name,
                'title': message.title,
                'message': message.message
            })

        return render(request, 'messages.html', {'user_messages': message_data})
    else:
        return render(request, 'messages.html', {'user_messages': None})



@login_required
def delete_messages(request):
    if request.method == 'POST':
        Message.objects.all().delete()  # Delete all messages
        return redirect('messages')  # Redirect to the messages list view
    else:
        # Handle GET request (though it should not happen in this case)
        return redirect('messages')  # Redirect to the messages list view