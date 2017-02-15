
class AbstractHandler(xml.sax.handler.ContentHandler):

    buffer = ''

    unknown_tags = []

    def __init__(self, exporter, stop_after=0, ignore_missing_tags=False):
        self.exporter = exporter
        self.stop_after = stop_after
        self.ignore_missing_tags = ignore_missing_tags


    def characters(self, data):
        self.buffer += data

    def endDocument(self):
        self.exporter.finish()
