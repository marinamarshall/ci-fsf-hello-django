from django.shortcuts import render
from .models import Item

# Create your views here.
def get_todo_list(request):
    """
    to do list
    """
    items = Item.objects.all()
    context = {
        'items' : items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    """
    add item
    """
    return render(request, 'todo/add_item.html')
    