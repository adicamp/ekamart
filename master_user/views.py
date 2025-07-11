from django.shortcuts import render

# def index(request):
    # return render(request, 'master_user/index.html')

def index(request):
    users = [
        {
            'name': 'Budi Santoso',
            'user_id': 'BS001',
            'status': True,
            'division': 'IT',
            'permissions': ['view', 'add', 'edit']
        },
        {
            'name': 'Siti Aminah',
            'user_id': 'SA002',
            'status': True,
            'division': 'HRD',
            'permissions': ['view', 'add']
        },
        {
            'name': 'Agus Wijaya',
            'user_id': 'AW003',
            'status': False,
            'division': 'Keuangan',
            'permissions': ['view']
        },
        {
            'name': 'Dewi Lestari',
            'user_id': 'DL004',
            'status': True,
            'division': 'Marketing',
            'permissions': ['view', 'edit']
        },
        {
            'name': 'Cahya Ramadhan',
            'user_id': 'CR005',
            'status': False,
            'division': 'IT',
            'permissions': ['view', 'delete']
        },
        {
            'name': 'Eka Putri',
            'user_id': 'EP006',
            'status': True,
            'division': 'HRD',
            'permissions': ['view', 'add', 'edit', 'delete']
        },
        {
            'name': 'Fajar Nugraha',
            'user_id': 'FN007',
            'status': True,
            'division': 'Keuangan',
            'permissions': ['view']
        },
        {
            'name': 'Gita Permata',
            'user_id': 'GP008',
            'status': False,
            'division': 'Marketing',
            'permissions': ['view', 'add']
        },
    ]
    context = {
        'users': users
    }
    return render(request, 'master_user/index.html', context)