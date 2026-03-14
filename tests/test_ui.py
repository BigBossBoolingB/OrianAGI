import unittest
from orianagi.app import app
import json

class TestOrianAGI_UI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'OrianAGI Genesis', response.data)

    def test_api_status(self):
        response = self.app.get('/api/status')
        data = json.loads(response.data)
        self.assertEqual(data['system_id'], "QAATA-GENESIS-V1.2")

    def test_api_nodes(self):
        response = self.app.get('/api/nodes')
        data = json.loads(response.data)
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0]['name'], "Denver Citadel")

    def test_api_poetic(self):
        response = self.app.post('/api/poetic',
                                 data=json.dumps({'theme': 'Universe'}),
                                 content_type='application/json')
        data = json.loads(response.data)
        self.assertIn('Hamiltonian', data['poem'])

if __name__ == '__main__':
    unittest.main()
