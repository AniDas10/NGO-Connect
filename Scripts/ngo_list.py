from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_df():
    paras = {23:0, 31:1, 41:2, 48:3, 53:4, 63:5, 69:6, 77:7, 79:8, 86:9, 94:10, 99:11, 104:12, 108:13, 115:14, 120:15, 123:16, 127:17, 130:18, 135:19}
    key_list = list(paras.keys())
    names = {}
    link = {}
    cause = {}
    city = {}
    details = {}
    url = "https://careerninja.in/achieve/social-sector/20-best-ngo-india-work/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for i,p in enumerate(soup.find_all('p')):
        for span in p.find_all('span'):
            if i in key_list:
                details[paras[i]] = span.text
    for i,h2 in enumerate(soup.find_all('h2')):
        for name in h2.find_all('a'):
            names[i-3] = name.text
            link[i-3] = name.get('href')
    for i,h4 in enumerate(soup.find_all('h4')):
        c = h4.text.split(':')
        if i == 40:
            break
        elif i%2 == 0:
            cause[int(i/2)] = c[1].strip()
        elif i%2 == 1:
            city[int(i/2 - 0.5)] = c[1].strip()
        
    data = [names, link, cause, city, details]
    dff = pd.DataFrame(data)
    df = dff.transpose()
    df.columns = ['Name', 'Link', 'Cause', 'City', 'Details']
    dic = {}
    dic = df.to_dict()
    return dic

get_df()