import unittest
from app import app  

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Flask test istemcisini başlat
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        # Ana sayfaya GET isteği gönder
        response = self.app.get('/')
        # HTTP durum kodunun 200 olduğunu doğrula
        self.assertEqual(response.status_code, 200)
        # Yanıtta bir HTML içeriğinin bulunduğunu kontrol et
        self.assertIn(b'class_names', response.data)  # Sayfanın yüklenip yüklenmediğini kontrol eder

    def test_analyze_endpoint_without_file(self):
        # Analyze endpointine POST isteği göndermeyi test et (dosya olmadan)
        response = self.app.post('/analyze')
        # Hata durumunu kontrol et
        self.assertEqual(response.status_code, 400)
        # Hata mesajının döndüğünü doğrula
        self.assertIn(b'error', response.data)

if __name__ == '__main__':
    unittest.main()
