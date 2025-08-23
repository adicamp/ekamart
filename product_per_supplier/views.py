from django.shortcuts import render
import random

def index(request):
    supplier = {
        'kode_supplier': 'SA0001',
        'nama_supplier': 'AJINOMOTO SALES INDONESIA PT',
        'status': True,
    }

    supplier_list = [
        {'kode_supplier': 'SA0001', 'nama_supplier': 'AJINOMOTO SALES INDONESIA PT', 'kategori': 'BKL dan Non BKL', 'status': True},
        {'kode_supplier': 'SR0001', 'nama_supplier': 'SARANA ABADI MAKMUR BERSAMA PT', 'kategori': 'BKL dan Non BKL', 'status': True},
        {'kode_supplier': 'SR0002', 'nama_supplier': 'MITRA JAYAPERSADA PT', 'kategori': 'BKL dan Non BKL', 'status': True},
        {'kode_supplier': 'SB0001', 'nama_supplier': 'DENNY SANJAYA (TELUR)', 'kategori': 'Non BKL', 'status': True},
        {'kode_supplier': 'SB0002', 'nama_supplier': 'CITRADIMENSI ARTHAL PT', 'kategori': 'BKL', 'status': True},
        {'kode_supplier': 'SB0003', 'nama_supplier': 'AKIRA KANIK INDAH PT', 'kategori': 'BKL dan Non BKL', 'status': True},
        {'kode_supplier': 'SA0002', 'nama_supplier': 'CHAROEN POKPHAND INDONESIA TBK PT', 'kategori': 'BKL dan Non BKL', 'status': True},
        {'kode_supplier': 'SA0003', 'nama_supplier': 'CITRA PUTRA TATAPERTAMA PT', 'kategori': 'BKL dan Non BKL', 'status': True},
        {'kode_supplier': 'SA0004', 'nama_supplier': '(D) AJINOMOTO SALES INDONESIA PT', 'kategori': 'BKL dan Non BKL', 'status': True},
        {'kode_supplier': 'SA0005', 'nama_supplier': 'MILLENIUM PHARMACON INTERNATIONAL TBK PT', 'kategori': 'BKL dan Non BKL', 'status': True},
        {'kode_supplier': 'SA0006', 'nama_supplier': 'INA PRIMA GRAFINOD PT', 'kategori': 'BKL dan Non BKL', 'status': True},
        {'kode_supplier': 'SA0007', 'nama_supplier': 'SO GOOD FOOD PT', 'kategori': 'BKL dan Non BKL', 'status': True},
        {'kode_supplier': 'SA0008', 'nama_supplier': 'DECHI SUKSES INDONESIA PT', 'kategori': 'BKL dan Non BKL', 'status': True},
        {'kode_supplier': 'SA0009', 'nama_supplier': 'KENKO SAHABAT INDONESIA PT', 'kategori': 'BKL dan Non BKL', 'status': True},
        {'kode_supplier': 'SA0010', 'nama_supplier': 'INBISCO NIAGATAMA SEMESTA PT', 'kategori': 'BKL dan Non BKL', 'status': True},
    ]

    products = [
        {
            'plu': '401032',
            'barcode': '8992770111005',
            'description': 'MAYUMI MAYONNAISE 100G SAC',
            'aktif': True,
        },
        {
            'plu': '518033',
            'barcode': '8992770061072',
            'description': 'SAJIKU TEPUNG BAKWAN 210G PCH',
            'aktif': False,
        },
        {
            'plu': '518034',
            'barcode': '8992770084064',
            'description': 'SAJIKU TEPUNG BUMBU SERBA GUNA',
            'aktif': True,
        },
        {
            'plu': '518035',
            'barcode': '8992770061041',
            'description': 'SAJIKU TEPUNG BUMBU GOLDEN CRISPY',
            'aktif': False,
        },
        {
            'plu': '523056',
            'barcode': '8992770096227',
            'description': 'SAORI SAUS TERIYAKI 135ML PET',
            'aktif': True,
        },
        {
            'plu': '525037',
            'barcode': '8992770096128',
            'description': 'SAORI SAUS TIRAM 133ML PET',
            'aktif': False,
        },
        {
            'plu': '518038',
            'barcode': '8992770054012',
            'description': 'SAJIKU BUMBU NASI GORENG AYAM',
            'aktif': True,
        },
        {
            'plu': '518039',
            'barcode': '8992770054036',
            'description': 'SAJIKU BUMBU NASI GORENG PEDAS',
            'aktif': False,
        },
        {
            'plu': '518040',
            'barcode': '8992770061058',
            'description': 'SAJIKU TEPUNG BUMBU GOLDEN CRISPY',
            'aktif': True,
        },
        {
            'plu': '111041',
            'barcode': '8992770011084',
            'description': 'AJINOMOTO MSG 100G PCH',
            'aktif': False,
        },
        {
            'plu': '398013',
            'barcode': '8992770434343',
            'description': 'PRODUK LAIN',
            'aktif': True,
        },
    ]

    context = {
        'supplier': supplier,
        'products': products,
        'supplier_list': supplier_list,
    }
    return render(request, 'product_per_supplier/index.html', context)