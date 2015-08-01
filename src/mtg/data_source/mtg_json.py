from urllib.request import urlopen
import json
import sqlite3 as lite

def GrabJson(url, local):
    response = urlopen(url)
    open(local,'wb').write(response.readall())

def MtgSetsInfo(local_json = 'AllSets.json'):
    import sys
    print(sys.cwd())
    all_sets = json.load(open(local_json,'r'))
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


