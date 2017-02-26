from django.contrib import admin
from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'done_check')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'task_id')


admin.site.register(Task, TaskAdmin)
admin.site.register(Comment, CommentAdmin)
