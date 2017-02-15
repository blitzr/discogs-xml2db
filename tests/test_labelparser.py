
import unittest

from gzip import GzipFile

from io import StringIO, BytesIO

try:
    from urllib2 import urlopen
except:
    from urllib.request import urlopen

import xml.sax

from discogslabelparser import LabelHandler
from jsonexporter import JsonConsoleExporter

from .utils import get_latest_dumps


class TestMasterHandler(unittest.TestCase):

    def test_parse_first(self):
        parser = xml.sax.make_parser()
        parser.setContentHandler(
            LabelHandler(
                JsonConsoleExporter(None),
                stop_after=0,
                ignore_missing_tags=True
            )
        )

        parser.parse(
            GzipFile(fileobj=urlopen(
                get_latest_dumps('labels')
            ))
        )

if __name__ == '__main__':
    unittest.main()
