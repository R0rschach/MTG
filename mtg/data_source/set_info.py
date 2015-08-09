import pkg_resources
from mtg.data_source.mtg_json import MtgJson
from collections import defaultdict


def MtgSetFormat(local_set_format = ''):
    if not local_set_format:
        text = pkg_resources.resource_string('mtg.resource','set_format.txt').decode('utf-8')
    else:
        text = open(local_set_format, 'r').read()

    dct = defaultdict(list)
    for line in text.split('\n'):
        if line.strip() == '':
            continue
        form, set_name = line.split('\t')
        dct[form].append(set_name)
    return dct

def MtgSetsInfo(local_json = ''):
    all_sets = MtgJson(local_json)
    for code, s in MtgJson().items():
        release_date = s['releaseDate']
        name = s['name']
        set_type = s['type']
        cards = len(s['cards'])
        yield (set_type, code, release_date, name, cards)


if __name__ == '__main__':
    for info in MtgSetsInfo():
        print(info)

