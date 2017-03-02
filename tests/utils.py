import requests
import re
import sys
from datetime import date
from xml.dom import minidom
from os import path


year = date.today().year
URL_LIST = "http://discogs-data.s3-us-west-2.amazonaws.com/?delimiter=/&prefix=data/{0}/".format(year)
URL_DIR = "http://discogs-data.s3-us-west-2.amazonaws.com/{0}"
PATTERN = r"discogs_[0-9]{8}_(artists|labels|masters|releases).xml.gz"

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)


def get_list():
    r = requests.get(URL_LIST)
    return r.text


def xml_extract_latest(text):
    dom = minidom.parseString(text)
    file_nodes = [getText(n.childNodes) for n in dom.getElementsByTagName('Key')]
    files = sorted(file_nodes, reverse=True)
    last4 = []
    for f in files:
        if re.search(PATTERN, f) is not None:
            last4.append(f)
        if len(last4) == 4:
            break

    return last4


def make_url(*chunks):
    for chunk in chunks:
        yield URL_DIR.format(chunk)

def get_latest_dumps(grep=None):
    xml = ''
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        with open(path.realpath("./tmp/ListBucketResult.xml")) as fxml:
            xml = fxml.read()
    else:
        xml = get_list()
    if grep:
        return [u for u in make_url(*xml_extract_latest(xml)) if grep in u][0]
    return make_url(*xml_extract_latest(xml))

if __name__ == "__main__":
    print('\n'.join(get_latest_dumps()))
