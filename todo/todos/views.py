from django.shortcuts import get_object_or_404, redirect, render 
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Comment, Task
from .forms import CommentForm, TaskForm


class IndexView(FormMixin, ListView):
    template_name = 'index.html'
    model = Task
    queryset = Task.objects.order_by('done_check', 'deadline')
    context_object_name = 'tasks'

    form_class = TaskForm

    def get_success_url(self):
        return reverse('index')

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST or None)
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class DetailView(FormMixin, DetailView):
    model = Task
    template_name = 'detail.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(task=self.object).order_by('-created_at')
        return context

    def get_success_url(self):
        return reverse('index')
        

    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.task = task
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def done(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.done_check = True
    task.save()
    return HttpResponseRedirect(reverse('index'))
    

