from django.shortcuts import render

def index(request):
    dc_data = {
        'kode_dc': 'DC.001',
        'nama_dc': 'GUDANG CIPUTAT',
        'alamat_dc': 'JL KH DEWANTARA NO. 12, RT.3/RW.7'
    }

    supplier_list = [
        {
            'id': '103018001',
            'nama_supplier': 'SUPPLIER CIPUTAT',
            'jadwal': {
                'senin': True,
                'selasa': True,
                'rabu': True,
                'kamis': True,
                'jumat': True,
                'sabtu': True,
                'minggu': True
            }
        },
        {
            'id': '103018002',
            'nama_supplier': 'SUPPLIER GADING',
            'jadwal': {
                'senin': False,
                'selasa': True,
                'rabu': True,
                'kamis': False,
                'jumat': True,
                'sabtu': False,
                'minggu': True
            }
        },
        {
            'id': '103018003',
            'nama_supplier': 'SUPPLIER REZEKI',
            'jadwal': {
                'senin': True,
                'selasa': True,
                'rabu': False,
                'kamis': True,
                'jumat': False,
                'sabtu': True,
                'minggu': False
            }
        },
        {
            'id': '103018004',
            'nama_supplier': 'SUPPLIER SEJAHTERA',
            'jadwal': {
                'senin': True,
                'selasa': False,
                'rabu': True,
                'kamis': True,
                'jumat': True,
                'sabtu': True,
                'minggu': False
            }
        },
        {
            'id': '103018005',
            'nama_supplier': 'SUPPLIER AMANAH',
            'jadwal': {
                'senin': False,
                'selasa': True,
                'rabu': False,
                'kamis': True,
                'jumat': False,
                'sabtu': False,
                'minggu': True
            }
        },
    ]

    hari_list = [
        'senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu'
    ]

    context = {
        'dc': dc_data,
        'supplier_list': supplier_list,
        'hari_list': hari_list
    }

    return render(request, 'supplier_reguler/index.html', context)