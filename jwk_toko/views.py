from django.shortcuts import render

def index(request):
    dc_data = {
        'kode_dc': 'DC.001',
        'nama_dc': 'GUDANG CIPUTAT',
        'alamat_dc': 'JL KH DEWANTARA NO. 12, RT.3/RW.7'
    }

    toko_list = [
        {
            'kode_toko': '103018001',
            'nama_toko': 'EKAMART CIPUTAT',
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
            'kode_toko': '103018002',
            'nama_toko': 'GADING MART',
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
            'kode_toko': '103018003',
            'nama_toko': 'REZEKI LANCAR',
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
            'kode_toko': '103018004',
            'nama_toko': 'SEJAHTERA GROUP',
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
            'kode_toko': '103018005',
            'nama_toko': 'AMANAH JAYA',
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
        'toko_list': toko_list,
        'hari_list': hari_list
    }

    return render(request, 'jwk_toko/index.html', context)