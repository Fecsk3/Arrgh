from django.db import models

class Board(models.Model):
    board_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Title(models.Model):
    title_name = models.CharField(max_length=100)
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='titles')

    def __str__(self):
        return self.name

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    description = models.TextField()
    title_id = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='tasks')
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name
