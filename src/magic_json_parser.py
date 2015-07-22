from urllib.request import urlopen
import json
import sqlite3 as lite

def InitDB(db_path):
    connection = lite.connect(db_path, timeout=10)
    cursor = connection.cursor()


def GrabJson(url, local):
    response = urlopen(url)
    open(local,'wb').write(response.readall())

def LoadSetsInfo(local_json):
    all_sets = json.load(open(local_json,'r'))
    for s in all_sets.values():
        code = s['code']
        release_date = s['releaseDate']
        name = s['name']
        set_type = s['type']
        cards = len(s['cards'])
        yield (set_type, code, release_date, name, cards)

def SaveSetsInfo(db_path, loader):
    try:
        print('Openning DB %s' % db_path)
        connection = lite.connect(db_path, timeout=10)
        cursor = connection.cursor()
        pattern = 'INSERT INTO mtgset VALUES(?, ?, ?, ?, ?, ?);'

        print('Insert Magic Set Records...')
        i = 0
        for set_type, code, release_date, name, cards in loader:
            print(set_type, code, release_date, name, cards)
            cursor.execute(pattern , (i, code, release_date, name, set_type, cards))
            i += 1

        connection.commit()
    except:
        print('MTG Set Info Dump Failed.')
    finally:
        print('Closing DB %s' % db_path)
        connection.close()
    pass

if __name__ == '__main__':
    url = r'http://mtgjson.com/json/AllSets.json'
    local_path = 'AllSets.json'
    db_path = r'mtg.db'
     
    GrabJson(url, local_path)
    SaveSetsInfo(db_path, LoadSetsInfo(local_path))

