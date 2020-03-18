import bs4 as bs
import urllib.request
import json

url = urllib.request.urlopen(
    'http://hanaslexis.com/cards/random').read()
soup = bs.BeautifulSoup(url, 'lxml')


def Crawler():
    viet = soup.find('p', id="vieKey").string
    eng = soup.find('div', id="engKey").find('span').string
    concept = soup.find('div', id="concept")
    context = concept.find('p').string
    example_eng = soup.find('div', id="examples").get_text()
    example_viet = soup.find('p', id="examples").get_text()

    # Define Data
    data = {viet: {
        "viet": viet,
        "eng": eng,
        "context": context,
        "example_eng": example_eng,
        "example_viet": example_viet
    }},
    
    with open('data.json', 'r', encoding='utf-8') as json_file:
        oldData = json.load(json_file)
    with open('data.json','w+') as json_file:
        data = oldData.append(data)
        jsoned_data = json.dumps(oldData, indent=True)
        json_file.write(jsoned_data)
if __name__ == '__main__':
    Crawler()
