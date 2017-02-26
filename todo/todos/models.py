from django.db import models
from datetime import datetime


class Task(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    done_check = models.BooleanField(default=False)
    deadline = models.DateField(default=None, blank=True)

    def __str__(self):
        return self.text

    def get_comment_count(self):
        return self.comment.count()


class Comment(models.Model):
    author = models.CharField(max_length=50)
    task = models.ForeignKey('todos.Task', related_name='comment')
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.text) if self.text else self.id
