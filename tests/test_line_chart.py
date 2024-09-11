import unittest
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

class LineChartTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_line_chart_status_code(self):
        response = self.app.get('/line_chart')
        self.assertEqual(response.status_code, 200)

    def test_line_chart_content(self):
        response = self.app.get('/line_chart')
        self.assertIn(b'Statistik Perkara Bulan', response.data)
        self.assertIn(b'Gugatan', response.data)
        self.assertIn(b'Permohonan', response.data)

    def test_line_chart_content_type(self):
        response = self.app.get('/line_chart')
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')

if __name__ == '__main__':
    unittest.main()