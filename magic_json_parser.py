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
        yield (set_type, code, release_date, name)

def SaveSetsInfo(db_path, loader):
    try:
        print('Openning DB %s' % db_path)
        connection = lite.connect(db_path, timeout=10)
        cursor = connection.cursor()
        pattern = 'INSERT INTO mtgset VALUES(?, ?, ?, ?, ?);'

        print('Insert Magic Set Records...')
        i = 0
        for set_type, code, release_date, name in loader:
            print(set_type, code, release_date, name)
            cursor.execute(pattern , (i, code, release_date, name, set_type))
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

