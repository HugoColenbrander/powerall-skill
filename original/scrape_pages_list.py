#!/usr/bin/env python3
"""Scrape Powerall developer docs via browser automation using hermes_tools terminal."""
import json, re, sys
from pathlib import Path

OUT = Path("/Users/hugoc/docs-powerall-nl/powerall-api-docs-raw.json")

pages = [
    ("Overview", "https://developers.powerall.nl/overview/"),
    ("Authentication", "https://developers.powerall.nl/overview/authentication/"),
    ("Pagination", "https://developers.powerall.nl/overview/pagination/"),
    ("Includes", "https://developers.powerall.nl/overview/includes/"),
    ("Filters", "https://developers.powerall.nl/overview/filters/"),
    ("Mutations", "https://developers.powerall.nl/overview/mutations/"),
    ("Contact Persons", "https://developers.powerall.nl/docs/entities/contact-persons/"),
    ("Contracts", "https://developers.powerall.nl/docs/entities/contracts/"),
    ("Deliveries", "https://developers.powerall.nl/docs/entities/deliveries/"),
    ("Delivery Addresses", "https://developers.powerall.nl/docs/entities/delivery-addresses/"),
    ("Files", "https://developers.powerall.nl/docs/entities/files/"),
    ("General", "https://developers.powerall.nl/docs/entities/general/"),
    ("Goods Receipts", "https://developers.powerall.nl/docs/entities/goods-receipts/"),
    ("Invoices", "https://developers.powerall.nl/docs/entities/invoices/"),
    ("Journals", "https://developers.powerall.nl/docs/entities/journals/"),
    ("Last Modified Rules", "https://developers.powerall.nl/docs/entities/last-modified-rules/"),
    ("Permissions", "https://developers.powerall.nl/docs/entities/permissions/"),
    ("Picklists", "https://developers.powerall.nl/docs/entities/picklists/"),
    ("Products", "https://developers.powerall.nl/docs/entities/products/"),
    ("Purchase Invoices", "https://developers.powerall.nl/docs/entities/purchase-invoices/"),
    ("Purchase Orders", "https://developers.powerall.nl/docs/entities/purchase-orders/"),
    ("Relations", "https://developers.powerall.nl/docs/entities/relations/"),
    ("Sales Orders", "https://developers.powerall.nl/docs/entities/sales-orders/"),
    ("Service Messages", "https://developers.powerall.nl/docs/entities/service-messages/"),
    ("Service Objects", "https://developers.powerall.nl/docs/entities/service-objects/"),
    ("Work Orders", "https://developers.powerall.nl/docs/entities/work-orders/"),
    ("Add-ons", "https://developers.powerall.nl/docs/entities/add-ons/"),
]

print(json.dumps({"pages": pages, "total": len(pages)}))
