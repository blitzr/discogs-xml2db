
import unittest

from gzip import GzipFile

from io import StringIO, BytesIO

try:
    from urllib2 import urlopen
except:
    from urllib.request import urlopen

import xml.sax

from .discogslabelparser import LabelHandler
from .jsonexporter import JsonConsoleExporter

from .utils import get_latest_dumps


# class TestLabelHandler(unittest.TestCase):

#     def test_parse_first(self):
#         parser = xml.sax.make_parser()
#         parser.setContentHandler(
#             LabelHandler(
#                 JsonConsoleExporter(None),
#                 stop_after=0,
#                 ignore_missing_tags=True
#             )
#         )

#         parser.parse(
#             GzipFile(fileobj=urlopen(
#                 get_latest_dumps('labels')
#             ))
#         )

# if __name__ == '__main__':
#     unittest.main()

import unittest

class TestsContainer(unittest.TestCase):
    longMessage = True

def make_test_function():
    def test(self):
        self.assertTrue(True)
    return test

if __name__ == '__main__':
    class TestExporter(JsonConsoleExporter):
        def storeLabel(self, label):
            setattr(TestsContainer, 'test_{0}'.format(label.name), make_test_function())

        parser = xml.sax.make_parser()
        parser.setContentHandler(
            LabelHandler(
                TestExporter(),
                stop_after=0,
                ignore_missing_tags=True
            )
        )

        parser.parse(
            GzipFile(fileobj=urlopen(
                get_latest_dumps('labels')
            ))
        )

    unittest.main()