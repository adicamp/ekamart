from django.shortcuts import render

# def index(request):
    # return render(request, 'master_user/index.html')

def index(request):
    users = [
        {'name': 'ARIEF FADHILAH', 'user_id': 'arief', 'status': True},
        {'name': 'ANDI WIJAYA', 'user_id': 'andi', 'status': False},
        {'name': 'RIZKY PRATAMA', 'user_id': 'rizky', 'status': True},
        {'name': 'BUDI SANTOSO', 'user_id': 'budi', 'status': False},
        {'name': 'SITI AMINAH', 'user_id': 'siti', 'status': True},
        {'name': 'DEWI LESTARI', 'user_id': 'dewi', 'status': False},
        {'name': 'AGUS SUPRIYADI', 'user_id': 'agus', 'status': True},
        {'name': 'RINA OKTAVIANI', 'user_id': 'rina', 'status': False},
        {'name': 'YUSUF HIDAYAT', 'user_id': 'yusuf', 'status': True},
        {'name': 'LINA MARDIANA', 'user_id': 'lina', 'status': False},
    ]
    context = {
        'users': users
    }
    return render(request, 'master_user/index.html', context)