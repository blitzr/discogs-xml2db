
import unittest

from gzip import GzipFile

try:
    from urllib import urlopen
except:
    from urllib.request import urlopen

import xml.sax

from discogsartistparser import ArtistHandler
from jsonexporter import JsonConsoleExporter

from .utils import get_latest_dumps


class TestMasterHandler(unittest.TestCase):

    def test_parse_first(self):
        parser = xml.sax.make_parser()
        parser.setContentHandler(
            ArtistHandler(
                JsonConsoleExporter(None),
                stop_after=0,
                ignore_missing_tags=True
            )
        )
        parser.parse(
            GzipFile(fileobj=urlopen(
                get_latest_dumps('artists')
            ))
        )

if __name__ == '__main__':
    unittest.main()
