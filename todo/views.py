from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.
def get_todo_list(request):
    """
    to do list
    """
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    """
    add item
    """
    if request.method == 'POST':
        name = request.POST.get('item_name')
        status = 'status' in request.POST
        Item.objects.create(name=name, status=status)

        return redirect('get_todo_list')
        form = ItemForm()
        context = {
            'form': form
        }
    return render(request, 'todo/add_item.html', context)
