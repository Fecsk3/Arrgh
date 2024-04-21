import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ahoy.settings')
django.setup()

from index.models import Team, TeamMember

def seed_data():
    team = Team.objects.create(senior_id=2)
    team_member = TeamMember.objects.create(user_id=3, team_id=1)

if __name__ == "__main__":
    seed_data()
