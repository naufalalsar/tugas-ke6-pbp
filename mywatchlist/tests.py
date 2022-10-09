from django.test import TestCase

# Create your tests here.
class TestUrl(TestCase):

    def test_url_html(self):
        response = self.client.get(("/mywatchlist/html/"))
        self.assertEqual(response.status_code, 200)

    def test_url_xml(self):
        response = self.client.get("/mywatchlist/xml/")
        self.assertEqual(response.status_code, 200)

    def test_url_json(self):
        response = self.client.get("/mywatchlist/json/")
        self.assertEqual(response.status_code, 200)
