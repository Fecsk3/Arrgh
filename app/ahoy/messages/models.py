from django.db import models

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    from_id = models.IntegerField(null=False)
    to_id = models.IntegerField(null=False)
    message = models.TextField()
    read = models.BooleanField(null=True, default=None)
    title = models.TextField(null=False)

