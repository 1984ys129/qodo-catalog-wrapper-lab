import unittest

from client import load_product


class Transport:
    def get(self, *, tenant, sku, timeout):
        return {"tenant": tenant, "sku": sku, "timeout": timeout}


class ClientTests(unittest.TestCase):
    def test_passes_normalized_catalog_identity_and_timeout(self):
        product = load_product(Transport(), "sample-tenant", "PART-01")
        self.assertEqual((product["tenant"], product["sku"]), ("sample-tenant", "part-01"))
        self.assertGreater(product["timeout"], 0)
        self.assertLessEqual(product["timeout"], 10)
