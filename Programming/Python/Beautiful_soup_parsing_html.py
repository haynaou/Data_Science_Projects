import requests,bs4
'''This function returns the price of the product'''

def ebay_price_tag(url):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')

    #get product_name
    product_name_tag = soup.select('#itemTitle')
    product_name = product_name_tag[0].contents[1]

    #get product_price
    price_tag = soup.select('#prcIsum')
    price = price_tag[0].text
    price = price.replace('US', '').replace('$', '').strip()

    #print product_name and produt price
    print('The price for', product_name, 'is:',price, '\n')



ebay_price_tag('https://www.ebay.com/itm/ZAFUAL-Womens-Rainbow-Lace-Up-Strapless-Bikini-Set-Swimwear-Beachwear-Bathing/133094614726?hash=item1efd0ea6c6%3Am%3Ams3dGRmQC682evviMXiVMQA&_trkparms=%2526rpp_cid%253D5d5409a4b7c89603f65788bd&var=432403281565')

ebay_price_tag('https://www.ebay.com/itm/ZAFUL-Vintage-Floral-Dot-Rockabilly-Skirt-A-line-Flared-Swing-Pleated-Midi-Dress/182501479443?_trkparms=aid%3D333200%26algo%3DCOMP.MBE%26ao%3D1%26asc%3D20171012094517%26meid%3D3bca2512e2864c009649fc4e8fa0fa87%26pid%3D100008%26rk%3D2%26rkt%3D12%26sd%3D133094614726%26itm%3D182501479443%26pg%3D2047675&_trksid=p2047675.c100008.m2219')