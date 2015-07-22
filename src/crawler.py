import lxml.html as LH
from urllib.request import urlopen
import re
text = open(r'/Users/asmodeus/GitHub/MTG/setlist.html','r').read()


def GrabTcgSetPriceSummary(page_url, set_name):
    """
    Grab a single set's cards prices from TCGPlayer's summary page
    page_url    string e.g. http://magic.tcgplayer.com/db/search_result.asp?Set_Name=Magic%202015%20(M15)
    set_name    string e.g. Magic 2015 (M15)
    """
    local_path = set_name + '.html'
    
    response = urlopen(page_url)
    open(local_path, 'wb').write(response.readall())

    html = LH.fromstring(open(local_path,'rb').read())
    cards = html.xpath('body/div/form/table[2]/tr')
    for row in cards:
        cleaned = [c.text_content().strip() for c in row.getchildren()]
        name, cost, set_name, rarity, high, mid, low = cleaned
        card_url = row.xpath('td[1]/a/@href')
        yield (name, cost, set_name, rarity, high, mid, low, card_url)

def GrabTcgSetList(page_url, dump_path):
    response = urlopen(page_url)
    open(dump_path, 'wb').write(response.readall())
    html = open(dump_path,'r').read()
    pattern = re.compile(r'href="(.*)">(.*)</a><BR>')
    set_list = pattern.findall(html)
    for href, set_name in set_list:
        yield set_name, href.replace(' ', '%20')

def GrabFishCardPriceHistory(set_name, card_name):
    """
    Grab a given card's price history from MTGOFish
    set_name string
    card_name string

    Sample Url : http://www.mtggoldfish.com/price/Dragons+of+Tarkir/Clone+Legion#online
    """
    pattern = "http://www.mtggoldfish.com/price/{0}/{1}#online" 
    url = str.format(pattern, set_name, card_name).replace(' ', '+')

    online = html[html.index('$(".price-sources-online").toggle(true);'):]
    for date, price in re.compile(r'd .*(20.+), (.*)\"').findall(online):
        yield (date, price)
    
if __name__ == '__main__':
    setlist_url = '/all_magic_sets.asp'
    tcg = r'http://magic.tcgplayer.com'
    local_setlist = r'set_list.txt'
    
    for set_name, set_url in GrabTcgSetList(tcg + setlist_url, local_setlist):
        print(set_name, set_url)
        for card in GrabTcgSetPriceSummary(tcg + set_url, set_name):
            print(card)
        break


