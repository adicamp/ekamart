from django.http import JsonResponse
from django.urls import reverse, NoReverseMatch


def safe_reverse(name: str, default: str | None = None):
    try:
        return reverse(name)
    except NoReverseMatch:
        return default or f"/{name.replace('.', '/')}/"


def menu_api_view(_request):
    # Dashboard (single root item)
    dashboard_item = {
        "key": "dashboard",
        "label": "Dashboard",
        "type": "item",
        "url": safe_reverse("dashboard.index"),
        "icon": "home",
    }
    master_children = [
        {
            "key": "max_inventory",
            "label": "Max Inventory",
            "type": "submenu",
            "icon": "inventory",
            "children": [
                {
                    "key": "max_inventory_dc",
                    "label": "Max Inventory DC",
                    "type": "item",
                    "url": safe_reverse("max_inventory_dc.index"),
                    "icon": "inventory_dc",
                },
                {
                    "key": "max_inventory_toko",
                    "label": "Max Inventory Toko",
                    "type": "item",
                    "url": safe_reverse("max_inventory_toko.index"),
                    "icon": "inventory_toko",
                },
            ],
        },
        {
            "key": "jwk_delivery_schedule",
            "label": "JWK - Delivery Schedule",
            "type": "submenu",
            "icon": "calendar",
            "children": [
                {
                    "key": "supplier_reguler",
                    "label": "Supplier Reguler",
                    "type": "item",
                    "url": safe_reverse("supplier_reguler.index"),
                    "icon": "supplier_reguler",
                },
                {
                    "key": "supplier_bkl",
                    "label": "Supplier BKL",
                    "type": "item",
                    "url": safe_reverse("supplier_bkl.index"),
                    "icon": "supplier_bkl",
                },
                {
                    "key": "jwk_toko",
                    "label": "JWK Toko",
                    "type": "item",
                    "url": safe_reverse("jwk_toko.index"),
                    "icon": "jwk_toko",
                },
            ],
        },
        {
            "key": "store_registration",
            "label": "Store Registration",
            "type": "item",
            "url": safe_reverse("store_registration.index"),
            "icon": "store_registration",
        },
        {
            "key": "product_per_supplier",
            "label": "Product Per Supplier",
            "type": "item",
            "url": safe_reverse("product_per_supplier.index"),
            "icon": "product_per_supplier",
        },
        {
            "key": "master_user",
            "label": "Master User",
            "type": "item",
            "url": safe_reverse("master_user.index"),
            "icon": "users",
        },
    ]

    planogram_children = [
        {
            "key": "master_rak",
            "label": "Rak",
            "type": "item",
            "url": safe_reverse("master_rak.index"),
            "icon": "rak",
        },
        {
            "key": "master_shelving",
            "label": "Shelving",
            "type": "item",
            "url": safe_reverse("master_shelving.index"),
            "icon": "shelving",
        },
    ]

    data = [
        dashboard_item,
        {
            "key": "master",
            "label": "Master",
            "type": "group",
            "icon": "folder",
            "children": master_children,
        },
        {
            "key": "planogram",
            "label": "Planogram",
            "type": "group",
            "icon": "planogram",
            "children": planogram_children,
        },
    ]
    return JsonResponse({"menu": data})
