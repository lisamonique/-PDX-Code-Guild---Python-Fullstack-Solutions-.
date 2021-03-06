
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import TodoItem, Priority

# Create your views here.

def index(request):

    todo_items = TodoItem.objects.filter(completed_date__isnull=True)
    completed_items = TodoItem.objects.filter(completed_date__isnull=False)
    priority_items = Priority.objects.all()

    context = {
        "todo_items": todo_items,
        "completed_items": completed_items,
        "priority_items": priority_items
    }
    return render(request, 'todo/index.html', context)

def create_list(request):
    form = request.POST

    todo_item = TodoItem()
    todo_item.description = form['description']
    
    priority_text = form['priority']
    priority_items = Priority.objects.get(name=priority_text)
    todo_item.priority = priority_items
    
    todo_item.save()

    return HttpResponseRedirect(reverse('index'))

def complete_todo(request, id):
    
    todo_item = TodoItem.objects.get(id=id)
    todo_item.completed_date = timezone.now()
    todo_item.save()

    return HttpResponseRedirect(reverse('index'))


def delete_todo(request, id):
    todo_item = TodoItem.objects.get(id=id)
    todo_item.delete()

    return HttpResponseRedirect(reverse('index'))