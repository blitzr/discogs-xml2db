
import unittest

from gzip import GzipFile

try:
    from urllib import urlopen
except:
    from urllib.request import urlopen

import xml.sax

from discogsreleaseparser import ReleaseHandler
from jsonexporter import JsonConsoleExporter

from .utils import get_latest_dumps


class TestReleaseHandler(unittest.TestCase):

    def test_parse_first(self):
        parser = xml.sax.make_parser()
        parser.setContentHandler(
            ReleaseHandler(
                JsonConsoleExporter(None),
                stop_after=0,
                ignore_missing_tags=True
            )
        )
        parser.parse(
            GzipFile(fileobj=urlopen(
                get_latest_dumps('releases')
            ))
        )

if __name__ == '__main__':
    unittest.main()