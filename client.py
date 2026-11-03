"""Catalog client using the shared service facade."""

from catalog.service import Catalog


def load_product(transport, tenant, sku):
    return Catalog(transport).get_product(tenant, sku)
