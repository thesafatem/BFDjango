from django.shortcuts import render


def todo(request):
    tasks = [
        {
            'task': 'task 1',
            'created': '10/09/2018',
            'due_on': '12/09/2018',
            'owner': 'admin',
            'mark': 'done'
        },
        {
            'task': 'task 2',
            'created': '10/09/2018',
            'due_on': '12/09/2018',
            'owner': 'admin',
            'mark': 'done'
        },
        {
            'task': 'task 3',
            'created': '10/09/2018',
            'due_on': '12/09/2018',
            'owner': 'admin',
            'mark': 'done'
        },
        {
            'task': 'task 4',
            'created': '10/09/2018',
            'due_on': '12/09/2018',
            'owner': 'admin',
            'mark': 'done'
        }
    ]
    return render(request, 'todo_list.html', context={'tasks': tasks})


def completed(request):
    tasks = [
        {
            'task': 'task 0',
            'created': '10/09/2018',
            'due_on': '12/09/2018',
            'owner': 'admin',
            'mark': 'not done'
        }
    ]
    return render(request, 'completed_todo_list.html', context={'tasks': tasks})