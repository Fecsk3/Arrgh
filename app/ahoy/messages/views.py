from django.db import connection
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User

@login_required
def user_list_view(request):
    is_staff_or_superuser = request.user.is_staff or request.user.is_superuser
    bitch = None
    user_messages = None
    user_id = request.user.id

    try:
        with connection.cursor() as cursor:
            # Felhasználóhoz tartozó üzenetek lekérése
            cursor.execute("SELECT username, title, message FROM messages JOIN auth_user ON messages.from_id = auth_user.id WHERE to_id = %s", [user_id])
            user_messages = cursor.fetchall()

            if request.user.is_staff:
                # Staffhoz tartozó csapatok lekérése
                cursor.execute("SELECT teams_id FROM index_team WHERE senior_id = %s", [user_id])
                team_rows = cursor.fetchall()
                team_ids = [row[0] for row in team_rows]

                # Csapatokhoz tartozó felhasználók lekérése
                cursor.execute("SELECT user_id FROM index_teammember WHERE team_id IN (%s)" % ', '.join(['%s'] * len(team_ids)), team_ids)
                team_user_rows = cursor.fetchall()
                team_user_ids = [row[0] for row in team_user_rows]

                # Felhasználók lekérése
                bitch = User.objects.filter(id__in=team_user_ids)

            elif request.user.is_superuser:
                # Admin felhasználók lekérése
                users = User.objects.filter(is_staff=True)
                return render(request, 'messages.html', {'user_messages': user_messages, 'members': users, 'is_staff_or_superuser': is_staff_or_superuser})

    except Exception as e:
        print(e)

    return render(request, 'messages.html', {'user_messages': user_messages, 'members': bitch, 'is_staff_or_superuser': is_staff_or_superuser})
    

@login_required
def send_message(request):
    is_staff_or_superuser = request.user.is_staff or request.user.is_superuser
    if request.method == 'POST':
        from_id = request.user.id 
        to_id = request.POST.get('members')
        title = request.POST.get('title')
        message = request.POST.get('message')  
        if title != "" and message != "":
            save_message(from_id, to_id, title, message)
            return render(request, 'messages.html')  
        else:
            return render(request, 'messages.html',{'is_staff_or_superuser':is_staff_or_superuser})
@login_required     
def save_message(from_id, to_id,title, message):
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO messages (from_id, to_id, message,read,title) VALUES (%s, %s, %s,false,%s)", [from_id, to_id, message,title])
    except Exception as e:
        print(e)


    
