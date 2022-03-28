from django.shortcuts import render

# Create your views here.
def get_todo_list(request):
    """
    to do list
    """
    return render(request, 'todo/todo_list.html')
