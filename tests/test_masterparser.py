
import unittest

from gzip import GzipFile

try:
    from urllib import urlopen
except:
    from urllib.request import urlopen

import xml.sax

from discogsmasterparser import MasterHandler
from jsonexporter import JsonConsoleExporter

from utils import get_latest_dumps


class TestMasterHandler(unittest.TestCase):

    def test_parse_first(self):
        parser = xml.sax.make_parser()
        parser.setContentHandler(
            MasterHandler(
                JsonConsoleExporter(None),
                stop_after=1,
                ignore_missing_tags=True
            )
        )
        parser.parse(
            GzipFile(fileobj=urlopen(
                get_latest_dumps('masters')
            ))
        )

if __name__ == '__main__':
    unittest.main()
