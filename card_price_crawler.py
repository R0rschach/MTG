import lxml.html as LH
from urllib.request import urlopen
import re
text = open(r'/Users/asmodeus/GitHub/MTG/setlist.html','r').read()


def GrabSingleSetPrice(page_url, set_name):
    # Grab a single set's cards prices from TCGPlayer's summary page
    # Sample Input: http://magic.tcgplayer.com/db/search_result.asp?Set_Name=Magic%202015%20(M15)
    local_path = set_name + '.html'
    
    response = urlopen(page_url)
    open(local_path, 'wb').write(response.readall())

    html = LH.fromstring(open(local_path,'r').read())
    cards = html.xpath('body/div/form/table')[1].findall('tr')
    for row in cards:
        cleaned = [c.text_content().strip() for c in row.getchildren()]
        name, cost, set_name, rarity, high, mid, low = cleaned
        yield (name, cost, set_name, rarity, high, mid, low)

def GrabSetList(page_url, dump_path):
    response = urlopen(page_url)
    open(dump_path, 'wb').write(response.readall())
    html = open(dump_path,'r').read()
    pattern = re.compile(r'href="(.*)">(.*)</a><BR>')
    set_list = pattern.findall(html)
    for href, set_name in set_list:
        yield set_name, href.replace(' ', '%20')

if __name__ == '__main__':
    setlist_url = '/all_magic_sets.asp'
    tcg = r'http://magic.tcgplayer.com'
    local_setlist = r'set_list.txt'
    
    for set_name, set_url in GrabSetList(tcg + setlist_url, local_setlist):
        print(set_name, set_url)
        for card in GrabSingleSetPrice(tcg + set_url, set_name):
            print(card)
        break


