import sys
from mtg.db.connection import connect
from mtg.data_source import set_info

def SaveSetsInfo(loader):
    try:
        print('Connect to DB mtg')
        connection = connect()
        cursor = connection.cursor()
       
        print('Insert Magic Set Records...')
        pattern = 'INSERT INTO mtgset (id, code, release_date, name, set_type, card_count) '
        pattern += 'VALUES(%s, %s, %s, %s, %s, %s);'

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
        print('Closing DB')
        connection.close()
    pass

def UpdateSetsFormat(set_format_file = ''):
    try:
        print('Loading Set Format Mapping')
        print()
        dct = set_info.MtgSetFormat(set_format_file)
        print('Block format contains %d set: [%s]' % ( len(dct['block']), ', '.join(dct['block'])))
        print('Standard format contains %d set: [%s]' % ( len(dct['standard']), ', '.join(dct['standard'])))
        print('Modern format contains %d set: [%s]' % ( len(dct['modern']), ', '.join(dct['modern'])))
        print()
        
        print('Openning DB')
        connection = connect()
        cursor = connection.cursor()
        
        print('Update Magic Set Format Eligibility Info...')
        for form, name_list in dct.items():
            pattern = str.format('UPDATE mtgset SET is_{0} = 1 WHERE name = %s;', form)
            for name in name_list:
                cursor.execute(pattern, (name,))
        connection.commit()
    except Exception as e:
        print('MTG Set Format Eligibility Info Dump Failed.')
        print(e)
    finally:
        print('Closing DB')
        connection.close()
    pass


if __name__ == '__main__':
    SaveSetsInfo(set_info.MtgSetsInfo())
    UpdateSetsFormat()
