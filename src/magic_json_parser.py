from urllib.request import urlopen
import json
import sqlite3 as lite

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
       
        print('Insert Magic Set Records...')
        pattern = 'INSERT INTO mtgset (id, code, release_date, name, set_type, card_count) '
        pattern += 'VALUES(?, ?, ?, ?, ?, ?);'

        i = 0
        for set_type, code, release_date, name, cards in loader:
            print(set_type, code, release_date, name, cards)
            cursor.execute(pattern , (i, code, release_date, name, set_type, cards))
            i += 1

        connection.commit()
    except Exception as e:
        print('MTG Set Info Dump Failed.')
        print(e)
    finally:
        print('Closing DB %s' % db_path)
        connection.close()
    pass

def UpdateSetsFormat(db_path):
    try:
        print('Loading Set Format Mapping')
        print()
        dct = {'block':[], 'standard':[], 'modern':[]}
        for row in open(r'../db/static/set_format.txt','r').readlines():
            form, name = row.split('\t')
            dct[form].append(name.strip())

        print('Block format contains %d set: [%s]' % ( len(dct['block']), ', '.join(dct['block'])))
        print('Standard format contains %d set: [%s]' % ( len(dct['standard']), ', '.join(dct['standard'])))
        print('Modern format contains %d set: [%s]' % ( len(dct['modern']), ', '.join(dct['modern'])))
        print()
        
        print('Openning DB %s' % db_path)
        connection = lite.connect(db_path, timeout=10)
        cursor = connection.cursor()
        
        print('Update Magic Set Format Eligibility Info...')
        for form, name_list in dct.items():
            pattern = str.format('UPDATE mtgset SET is_{0} = 1 WHERE name = ?;', form)
            for name in name_list:
                cursor.execute(pattern, (name,))
        connection.commit()
    except Exception as e:
        print('MTG Set Format Eligibility Info Dump Failed.')
        print(e)
    finally:
        print('Closing DB %s' % db_path)
        connection.close()
    pass


if __name__ == '__main__':
    url = r'http://mtgjson.com/json/AllSets.json'
    local_path = '../AllSets.json'
    db_path = r'../db/mtg.db'
     
    GrabJson(url, local_path)
    SaveSetsInfo(db_path, LoadSetsInfo(local_path))
    UpdateSetsFormat(db_path)

