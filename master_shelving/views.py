from django.shortcuts import render
from datetime import datetime

DUMMY_SHELVING_DATA = [
    {'id': 1, 'rak': 'A1', 'shelving': 'S01', 'lubang': 'L01', 'tgl_update': datetime.now().date()},
    {'id': 2, 'rak': 'A1', 'shelving': 'S01', 'lubang': 'L02', 'tgl_update': datetime.now().date()},
    {'id': 3, 'rak': 'B2', 'shelving': 'S05', 'lubang': 'L10', 'tgl_update': datetime.now().date()},
    {'id': 4, 'rak': 'C3', 'shelving': 'S12', 'lubang': 'L03', 'tgl_update': datetime.now().date()},
    {'id': 5, 'rak': 'A1', 'shelving': 'S02', 'lubang': 'L01', 'tgl_update': datetime.now().date()},
]

# Create your views here.
def index(request):
    shelving_data = DUMMY_SHELVING_DATA
    context = {
        'now': datetime.now(),
        'shelving_data': shelving_data,
    }
    return render(request, 'master_shelving/index.html', context)