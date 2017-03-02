
import unittest

import json

from jsonexporter import JsonConsoleExporter


class TestJsonConsoleExporter(unittest.TestCase):

    @staticmethod
    def assertIsJson(text):
        try:
            json.loads(text)
        except:
            return False
        return True

    @unittest.mock('print')
    def test_empty(self, p):
        self.assertIsJson(
            JsonConsoleExporter.
        )