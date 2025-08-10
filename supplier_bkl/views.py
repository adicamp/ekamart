from django.shortcuts import render

def index(request):
    supplier_list = [
        {
            'kode_supplier': 'SUP.001',
            'nama_supplier': 'PT. MAKMUR SEJAHTERA',
            'alamat_supplier': 'JL MERDEKA NO. 45, RT.2/RW.5',
            'nama_singkat': 'MAKMUR',
            'lead_time': 2
        },
        {
            'kode_supplier': 'SUP.002',
            'nama_supplier': 'CV. SENTOSA ABADI',
            'alamat_supplier': 'JL. RAYA PASAR MINGGU NO. 12',
            'nama_singkat': 'SENTOSA',
            'lead_time': 3
        },
        {
            'kode_supplier': 'SUP.003',
            'nama_supplier': 'UD. BERKAH JAYA',
            'alamat_supplier': 'JL. KEBON JERUK NO. 8',
            'nama_singkat': 'BERKAH',
            'lead_time': 1
        },
        {
            'kode_supplier': 'SUP.004',
            'nama_supplier': 'PT. SUKSES MAJU',
            'alamat_supplier': 'JL. PELANGI INDAH NO. 23',
            'nama_singkat': 'SUKSES',
            'lead_time': 4
        },
        {
            'kode_supplier': 'SUP.005',
            'nama_supplier': 'CV. ANUGERAH MULIA',
            'alamat_supplier': 'JL. CENDANA NO. 17',
            'nama_singkat': 'ANUGERAH',
            'lead_time': 2
        }
    ]

    supplier_data = {
            'kode_supplier': 'SUP.001',
            'nama_supplier': 'PT. MAKMUR SEJAHTERA',
            'alamat_supplier': 'JL MERDEKA NO. 45, RT.2/RW.5',
            'nama_singkat': 'MAKMUR',
            'lead_time': 2
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
        'supplier': supplier_data,
        'supplier_list': supplier_list,
        'toko_list': toko_list,
        'hari_list': hari_list
    }

    return render(request, 'supplier_bkl/index.html', context)