from django.shortcuts import render

def index(request):
    stores = [
        {
            'kode_toko': 'TK001',
            'nama_toko': 'Toko Sukses Makmur',
            'tanggal_go': '2024-06-01',
            'kode_registrasi': 'REG001'
        },
        {
            'kode_toko': 'TK002',
            'nama_toko': 'Toko Maju Bersama',
            'tanggal_go': '2024-06-02',
            'kode_registrasi': 'REG002'
        },
        {
            'kode_toko': 'TK003',
            'nama_toko': 'Toko Sentosa',
            'tanggal_go': '2024-06-03',
            'kode_registrasi': 'REG003'
        },
        {
            'kode_toko': 'TK004',
            'nama_toko': 'Toko Berkah Abadi',
            'tanggal_go': '2024-06-04',
            'kode_registrasi': 'REG004'
        },
        {
            'kode_toko': 'TK005',
            'nama_toko': 'Toko Sejahtera',
            'tanggal_go': '2024-06-05',
            'kode_registrasi': 'REG005'
        },
        {
            'kode_toko': 'TK006',
            'nama_toko': 'Toko Amanah',
            'tanggal_go': '2024-06-06',
            'kode_registrasi': 'REG006'
        },
        {
            'kode_toko': 'TK007',
            'nama_toko': 'Toko Jaya Sentosa',
            'tanggal_go': '2024-06-07',
            'kode_registrasi': 'REG007'
        },
        {
            'kode_toko': 'TK008',
            'nama_toko': 'Toko Mulia',
            'tanggal_go': '2024-06-08',
            'kode_registrasi': 'REG008'
        },
    ]
    context = {
        'stores': stores
    }
    return render(request, 'store_registration/index.html', context)