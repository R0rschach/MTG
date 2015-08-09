import pkg_resources
import json
from urllib.request import urlopen

default_url = r'http://mtgjson.com/json/AllSets.json'
default_local = pkg_resources.resource_filename('mtg.resource','AllSets.json')

def GrabJson(url = default_url, local = default_local):
    response = urlopen(url)
    open(local,'wb').write(response.readall())

def MtgJson(local_json = ''):
    if not local_json:
        text = pkg_resources.resource_string('mtg.resource', 'AllSets.json').decode('utf-8')
    else:
        text = open(local_json,'r').read()

    dct = {}
    for mtg_set in json.loads(text).values():
        dct[mtg_set['code']] = mtg_set
    return dct

if __name__ == '__main__':
    GrabJson()
