from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    racks = [
        {
            'id': 1,
            'rack': 'Rack A1',
            'last_updated': '2024-06-01',
            'user': 'John Doe'
        },
        {
            'id': 2,
            'rack': 'Rack B2',
            'last_updated': '2024-06-03',
            'user': 'Jane Smith'
        },
        {
            'id': 3,
            'rack': 'Rack C3',
            'last_updated': '2024-05-28',
            'user': 'Michael Johnson'
        },
        {
            'id': 4,
            'rack': 'Rack D4',
            'last_updated': '2024-06-02',
            'user': 'Emily Davis'
        },
        {
            'id': 5,
            'rack': 'Rack E5',
            'last_updated': '2024-05-30',
            'user': 'William Brown'
        },
        {
            'id': 6,
            'rack': 'Rack F6',
            'last_updated': '2024-06-04',
            'user': 'Olivia Wilson'
        },
        {
            'id': 7,
            'rack': 'Rack G7',
            'last_updated': '2024-05-29',
            'user': 'James Miller'
        },
        {
            'id': 8,
            'rack': 'Rack H8',
            'last_updated': '2024-06-01',
            'user': 'Sophia Anderson'   
        },
    ]

    users = [
        {'id': 'user1', 'name': 'Admin'},
        {'id': 'user2', 'name': 'John Doe'},
        {'id': 'user3', 'name': 'Jane Smith'},
        {'id': 'user4', 'name': 'Guest User'},
    ]
    context = {
        'now': datetime.now(),
        'racks': racks,
        'users': users,
    }
    return render(request, 'master_rak/index.html', context)
