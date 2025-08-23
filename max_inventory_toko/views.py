from django.shortcuts import render

def index(request):
    filter_list = [
        {'kode_filter': '0', 'nama_filter': 'NON KATEGORI'},
        {'kode_filter': '1', 'nama_filter': 'RTD COFFEE'},
        {'kode_filter': '2', 'nama_filter': 'RTD TEA'},
        {'kode_filter': '3', 'nama_filter': 'CARBONATED DRINK'},
        {'kode_filter': '4', 'nama_filter': 'MINERAL WATER'},
        {'kode_filter': '5', 'nama_filter': 'ISOTONIC DRINK'},
        {'kode_filter': '6', 'nama_filter': 'SYRUP'},
        {'kode_filter': '7', 'nama_filter': 'SKM (SIGARET KRETEK MES)'},
        {'kode_filter': '8', 'nama_filter': 'SPM (SIGARET PUTIH MESIN)'},
        {'kode_filter': '9', 'nama_filter': 'INSTANT NOODLE CUP'},
        {'kode_filter': '10', 'nama_filter': 'PASTA'},
        {'kode_filter': '11', 'nama_filter': 'MARGARINE & BUTTER'},
        {'kode_filter': '12', 'nama_filter': 'PALM COOKING OIL'},
        {'kode_filter': '13', 'nama_filter': 'INSTANT COFFEE MIX'},
        {'kode_filter': '14', 'nama_filter': 'BAG TEA'},
        {'kode_filter': '15', 'nama_filter': 'INSTANT TEA'},
        {'kode_filter': '16', 'nama_filter': 'CREAM DETERGENT'},
        {'kode_filter': '17', 'nama_filter': 'LIQUID DETERGENT'},
        {'kode_filter': '18', 'nama_filter': 'POWDER DETERGENT'},
        {'kode_filter': '19', 'nama_filter': 'SHAMPOO'},
        {'kode_filter': '20', 'nama_filter': 'TOOTH PASTE'},
        {'kode_filter': '22', 'nama_filter': 'TAKE HOME ICE CREAM'}
    ]

    toko_data = {
        'kode_toko': '10101001',
        'nama_toko': '3SMART GALAXY CITY',
        'alamat_toko': 'RUKO GRAND GALAXY CITY BLOK RGG NO 33',
        'jenis_toko': 'N',
        'type_toko': 'A'
    }

    toko_list = [
        {'kode_toko': '10101002', 'nama_toko': 'SMART CITY MALL'},
        {'kode_toko': '10101003', 'nama_toko': 'GALAXY SUPERMARKET'},
        {'kode_toko': '10101004', 'nama_toko': 'TOKO INDAH'},
        {'kode_toko': '10101005', 'nama_toko': 'MINIMART CENTRAL'},
        {'kode_toko': '10101006', 'nama_toko': 'TOKO MAJU JAYA'},
        {'kode_toko': '10101007', 'nama_toko': 'SUPERMARKET SEJAHTERA'},
        {'kode_toko': '10101008', 'nama_toko': 'TOKO HEMAT'}
    ]


    barang_list = [
        {
            'plu': 100001,
            'description': 'ABC KDRI MIX PACK 10X25GR PCK',
            'tag': 'normal',
            'class': 1,
            'last_cost': 8925.61,
            'avg_cost': 8925.61,
            'sales_qty_3_mo': 0,
            'sales_qty_2_mo': 2,
            'sales_qty_1_mo': 0,
            'min_dis': 0,
            'qty': 10000,
            'rp_max_awal': 0.0,
            'tgl_rubah': '26/09/2017'
        },
        {
            'plu': 100002,
            'description': 'ABC KDRI MOCXA 27 G SAC',
            'tag': 'medium',
            'class': 1,
            'last_cost': 853.63,
            'avg_cost': 853.63,
            'sales_qty_3_mo': 0,
            'sales_qty_2_mo': 1,
            'sales_qty_1_mo': 0,
            'min_dis': 0,
            'qty': 9500,
            'rp_max_awal': 0.0,
            'tgl_rubah': '26/09/2017'
        },
        {
            'plu': 100003,
            'description': 'ABC SQUASH MANGGA 525 ML BTL',
            'tag': 'normal',
            'class': 1,
            'last_cost': 8181.82,
            'avg_cost': 8181.82,
            'sales_qty_3_mo': 0,
            'sales_qty_2_mo': 1,
            'sales_qty_1_mo': 0,
            'min_dis': 0,
            'qty': 10000,
            'rp_max_awal': 0.0,
            'tgl_rubah': '26/09/2017'
        },
        {
            'plu': 100004,
            'description': 'ABC SQUASH ORANGE 525 ML BTL',
            'tag': 'fast',
            'class': 1,
            'last_cost': 9669.42,
            'avg_cost': 9669.42,
            'sales_qty_3_mo': 0,
            'sales_qty_2_mo': 1,
            'sales_qty_1_mo': 0,
            'min_dis': 0,
            'qty': 10000,
            'rp_max_awal': 0.0,
            'tgl_rubah': '26/09/2017'
        },
        {
            'plu': 114001,
            'description': 'AQUA AIR MINERAL PET 1500 ML BTL',
            'tag': 'normal',
            'class': 1,
            'last_cost': 3254.54,
            'avg_cost': 3251.29,
            'sales_qty_3_mo': 0,
            'sales_qty_2_mo': 1,
            'sales_qty_1_mo': 0,
            'min_dis': 0,
            'qty': 10000,
            'rp_max_awal': 0.0,
            'tgl_rubah': '26/09/2017'
        },
    ]

    context = {
        'toko': toko_data,
        'filter_list': filter_list,
        'barang_list': barang_list,
        'toko_list': toko_list,
    }

    return render(request, 'max_inventory_toko/index.html', context)