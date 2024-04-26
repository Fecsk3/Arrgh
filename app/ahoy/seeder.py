import os
import django
from django.db.utils import IntegrityError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ahoy.settings')
django.setup()

from django.contrib.auth.models import User

users_data = [
    {'username': 'birger', 'first_name': 'Gergő', 'last_name': 'Birinyi', 'email': 'birger@example.com', 'password': 'birger', 'is_superuser': True},
    {'username': 'balint', 'first_name': 'Bálint', 'last_name': 'Katona', 'email': 'balint@example.com', 'password': 'balint', 'is_staff': True},
    {'username': 'staff', 'first_name': 'Staff', 'last_name': 'Staff', 'email': 'staff@example.com', 'password': 'staff', 'is_staff': True},
    {'username': 'drntth', 'first_name': 'Dorina', 'last_name': 'Tóth', 'email': 'drntth@example.com', 'password': 'drntth'},
    {'username': 'valesz', 'first_name': 'Valentin', 'last_name': 'Sipos', 'email': 'valesz@example.com', 'password': 'valesz'},
    {'username': 'pali', 'first_name': 'Bálint', 'last_name': 'Kovácspál', 'email': 'pali@example.com', 'password': 'pali'},
]

try:
    for data in users_data:
        is_superuser = data.pop('is_superuser', False)
        is_staff = data.pop('is_staff', False)
        try:
            user = User.objects.create_user(**data)
            if is_superuser:
                user.is_superuser = True
                user.save()
            if is_staff:
                user.is_staff = True
                user.save()
        except IntegrityError:
            print(f'Az adat már szerepel a táblában: {data["username"]}')
            continue
except Exception as e:
    print(f'Hiba történt az adatok feltöltésekor: {e}')
else:
    print('Befejezve')

