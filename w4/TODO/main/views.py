from django.shortcuts import render
from main.models import List, Task


def todo(request, list_id):
    tasks = Task.objects.filter(list=list_id, mark=False)
    # tasks_json = [t.to_json for t in tasks]
    return render(request, 'todo_list.html', context={'tasks': tasks, 'list': list_id})
    # [
    #     {
    #         'task': 'task 1',
    #         'created': '10/09/2018',
    #         'due_on': '12/09/2018',
    #         'owner': 'admin',
    #         'mark': 'done'
    #     },
    #     {
    #         'task': 'task 2',
    #         'created': '10/09/2018',
    #         'due_on': '12/09/2018',
    #         'owner': 'admin',
    #         'mark': 'done'
    #     },
    #     {
    #         'task': 'task 3',
    #         'created': '10/09/2018',
    #         'due_on': '12/09/2018',
    #         'owner': 'admin',
    #         'mark': 'done'
    #     },
    #     {
    #         'task': 'task 4',
    #         'created': '10/09/2018',
    #         'due_on': '12/09/2018',
    #         'owner': 'admin',
    #         'mark': 'done'
    #     }
    # ]
    # return render(request, 'todo_list.html', context={'tasks': tasks})


def completed(request, list_id):
    tasks = Task.objects.filter(list=list_id, mark=True)
    return render(request, 'completed_todo_list.html', context={'tasks': tasks, 'list': list_id})
    # return render(request, 'completed_todo_list.html', context={'tasks': tasks})