# Generated by Django 3.2.12 on 2024-04-18 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('goal', models.TextField()),
                ('target_users', models.TextField()),
                ('problem_motivation', models.TextField()),
                ('technical_stack', models.TextField()),
                ('key_features', models.TextField()),
                ('deliverables', models.TextField()),
                ('timeline', models.TextField()),
                ('additional_info', models.TextField(blank=True)),
            ],
        ),
    ]
