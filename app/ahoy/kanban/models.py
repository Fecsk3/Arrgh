from django.db import models
from django.contrib.auth.models import User
from index.models import Team

class Board(models.Model):
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(Team, on_delete=models.CASCADE, to_field='teams_id')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Column(models.Model):
    title = models.CharField(max_length=100)
    board = models.ForeignKey(Board, related_name='columns', on_delete=models.CASCADE)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    column = models.ForeignKey(Column, related_name='cards', on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    color = models.CharField(max_length=7, default="#14BDEB", null=True)

    def __str__(self):
        return self.title
