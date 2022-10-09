from django.test import TestCase
from katalog.models import CatalogItem

class CatalogItemTestCase(TestCase):

    fixtures = ['initial_catalog_data.json']

    def test_modelCreated(self):
        catalog = CatalogItem.objects.all()
        size = 0
        for item in catalog :
            size+=1
        self.assertTrue(size >= 1)

    def test_modelHaveTheCorrectTypeAndHaveTheCorrectAttribute(self):
        catalog = CatalogItem.objects.all()
        for item in catalog :
            self.assertTrue(isinstance(item.item_name, str))
            self.assertTrue(isinstance(item.item_price, int))
            self.assertTrue(isinstance(item.item_url, str))
            self.assertTrue(isinstance(item.rating, int))
            self.assertTrue(isinstance(item.item_stock, int))
            self.assertTrue(isinstance(item.description, str))