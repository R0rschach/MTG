import json
import pkg_resources
from collections import defaultdict
from mtg.data_source.mtg_json import MtgJson


def MtgCardInfo(local_json = ''):
    for set_code, mtg_set in MtgJson(local_json).items():
        for card in mtg_set['cards']:
            name = card['name']
            mana_cost = card['manaCost'] if 'manaCost' in card else None
            cmc = card['cmc'] if 'cmc' in card else None
            colors = card['colors'] if 'colors' in card else None
            card_type = card['type'] if 'type' in card else None
            supertypes = card['supertypes'] if 'supertypes' in card else None
            types = card['types'] if 'types' in card else None
            subtypes = card['subtypes'] if 'subtypes' in card else None
            rarity = card['rarity'] if 'rarity' in card else None
            artist = card['artist']
            set_number = card['number'] if 'number' in card else None
            power = card['power'] if 'power' in card else None
            toughness = card['toughness'] if 'toughness' in card else None
            multiverseid = card['multiverseid'] if 'multiverseid' in card else None
            yield (name, mana_cost, cmc, card_type, colors, supertypes, types, subtypes, rarity, artist, set_code, set_number, power, toughness, multiverseid)

if __name__ == '__main__':
    card_gen = MtgCardInfo()
    i = 0
    for card in card_gen:
        i += 1
    print(i)

