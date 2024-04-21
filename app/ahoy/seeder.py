import os
import django
from django.db.utils import IntegrityError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ahoy.settings')
django.setup()

from django.contrib.auth.models import User

users_data = [
    {'username': 'felhasznalo', 'first_name': 'Elek', 'last_name': 'Vicc', 'email': 'viccelek@example.com', 'password': 'jelszo'},
    {'username': 'imi', 'first_name': 'Imre', 'last_name': 'Fütty', 'email': 'futtyimre@example.com', 'password': 'password'},
    {'username': 'admin', 'first_name': 'Admin', 'last_name': 'Admin', 'email': 'admin@example.com', 'password': 'admin', 'is_superuser': True},
    {'username': 'senior', 'first_name': 'Bélus', 'last_name': 'Ka', 'email': 'beluska@example.com', 'password': 'senior', 'is_superuser': True},
    {'username': 'ize', 'first_name': 'Ize', 'last_name': 'Bize', 'email': 'izeke@example.com', 'password': 'ize'},
    {'username': 'tunya', 'first_name': 'Tunya', 'last_name': 'Csap', 'email': 'Tunyacsap@example.com', 'password': 'tunya'},
]

try:
    for data in users_data:
        is_superuser = data.pop('is_superuser', False)
        try:
            user = User.objects.create_user(**data)
            if is_superuser:
                user.is_superuser = True
                user.save()
        except IntegrityError:
            print(f'Az adat már szerepel a táblában: {data["username"]}')
            continue
except Exception as e:
    print(f'Hiba történt az adatok feltöltésekor: {e}')
else:
    print('Az adatok már feltöltve')
