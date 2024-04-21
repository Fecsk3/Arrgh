from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    goal = models.TextField()
    target_users = models.TextField()
    problem_motivation = models.TextField()
    technical_stack = models.TextField()
    key_features = models.TextField()
    deliverables = models.TextField()
    timeline = models.TextField()
    additional_info = models.TextField(blank=True) 