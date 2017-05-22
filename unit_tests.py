
import unittest
import time
from datetime import datetime
from flask import json
from crawler import app

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.start_time = time.time()

    def test_error(self):
        """Test that 404 error message is correct"""
        response = self.app.get('/?url=http://www.google.fi/asdfg')
        data = response.data
        self.assertEqual("404: Requested URL is Not Found", str(data))

    def test_data(self):
        """Test that all the required data is available"""
        self.app.get('/?url=http://www.google.com')
        response = self.app.get('/?url=http://www.google.fi')
        data = json.loads(response.data)
        timer = round(time.time() - self.start_time)
        self.assertEqual(data[u'page_title'], "Google")
        self.assertEqual(data[u'requests_done'], 2)
        self.assertEqual(len(data[u'found_links']), 13)
        self.assertEqual(len(data[u'meta_data']), 2)
        self.assertEqual(data[u'link_counter'], 26)
        self.assertEqual(round(data[u'app_timer']), timer)
        self.assertEqual(data[u'system_time'], datetime.utcnow().isoformat())


if __name__ == '__main__':
    unittest.main()
