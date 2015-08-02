from urllib.request import urlopen
import json, os, sys, pkg_resources
import sqlite3 as lite

package_directory = os.path.dirname(os.path.abspath(__file__))

def GrabJson(url, local):
    response = urlopen(url)
    open(local,'wb').write(response.readall())

def MtgSetsInfo(local_json = ''):
    if not local_json:
        text = pkg_resources.resource_string('mtg.resource', 'AllSets.json').decode('utf-8')
    else:
        text = open(local_json,'r').read()
    all_sets = json.loads(text)
    for s in all_sets.values():
        code = s['code']
        release_date = s['releaseDate']
        name = s['name']
        set_type = s['type']
        cards = len(s['cards'])
        yield (set_type, code, release_date, name, cards)


if __name__ == '__main__':
    url = r'http://mtgjson.com/json/AllSets.json'
    local_path = '../AllSets.json'
    db_path = r'../db/mtg.db'
    set_format_file = r'../db/static/set_format.txt'
     
    GrabJson(url, local_path)
    SaveSetsInfo(db_path, LoadSetsInfo(local_path))
    UpdateSetsFormat(db_path, set_format_file)


