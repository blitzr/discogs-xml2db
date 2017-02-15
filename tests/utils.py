
from xml.sax.handler import ContentHandler

try:
    from urllib import urlopen
except:
    from urllib.request import urlopen

import xml.sax


def get_latest_dumps(grep=None):
    class urlExtractor(ContentHandler):
        def __init__(self, urls):
            self.buffer = ""
            self.urls = urls

        def startElement(self, name, attrs):
            if name != 'Key':
                self.buffer = ""

        def characters(self,ch):
            if ch != '"':
                self.buffer = ch

        def endElement (self, name):
            if name == 'Key' and self.buffer.endswith('.xml.gz'):
                self.urls.append("http://discogs-data.s3-us-west-2.amazonaws.com/" + self.buffer)
                self.buffer = ""
    urls = []
    parser = xml.sax.make_parser()
    parser.setContentHandler(urlExtractor(urls))
    parser.parse(
        urlopen("http://discogs-data.s3-us-west-2.amazonaws.com/?delimiter=/&prefix=data/")
    )

    if grep:
        return [e for e in sorted(urls, )[-4:] if grep in e][0]

    return sorted(urls, )[-4:]

if __name__ == "__main__":
    print(get_latest_dumps('labels'))