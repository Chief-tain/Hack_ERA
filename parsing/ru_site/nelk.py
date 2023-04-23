import requests
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint
import unicodedata

PARSING_MOD = "lxml"

def get_soup(strURL : str) -> BeautifulSoup:
    try:
        response = requests.get(strURL)
        print('Status code :', response.status_code, 'for', strURL)
    except:
        print("Connection error")
    soup = BeautifulSoup(response.text, PARSING_MOD) # "html.parser"
    return soup        

def get_currentPart(soup : BeautifulSoup, strTagName : str, strClassName : str) -> BeautifulSoup: 
    soup_copy = soup
    soup_copy = soup.findAll(strTagName, class_=strClassName)  
    return BeautifulSoup(str(soup_copy), PARSING_MOD)

def get_hrefs( soup : BeautifulSoup) -> list:
    soup = get_currentPart(soup, 'div', 'product-item')
    listHrefs = []
    for link in soup.find_all('a'):
        listHrefs.append(link.get('href'))
    return listHrefs

def separate_href(hrefs : list) -> list : 
    result = []
    for href in hrefs:
        result.append( href.split('?')[0] )
    return result

def normolize_list_text(list_text : list) -> list:
    result = []
    for item in list_text:
        result = unicodedata.normalize("NFKD", item)
    return result

def set_dict(keys : list, values : list) -> dict:
    result = {}
    for i in range( len(keys) ):
        result[keys[i]] = values[i]
    return result

def get_emptyDataframe( listColoms : list) -> pd.DataFrame:
    df = pd.DataFrame(dict(zip(listColoms, []*len(listColoms))))
    return df

def make_jsonFile( df : pd.DataFrame, strFileName : str, strOrient = 'records'):
    path = __file__[:__file__.rfind('\\')] + '\\' + strFileName + '.json'
    with open(  path,'w', encoding='utf-8') as file:
        isWrited = file.write(df.to_json(force_ascii=False, indent=3, orient=strOrient))
        if isWrited : print(f'Successfully recorded in {path}')

def get_main_href(href : str) -> str:
    index = [i for i in range(len(href)) if href.startswith('/', i)]
    return href[:index[2]]

def main() -> None:
    listZeroPages_url = [
                        'https://www.dji.com/ru/products/camera-drones?site=brandsite&from=nav',
                        'https://www.dji.com/ru/products/handheld-imaging-devices?site=brandsite&from=nav'
                    ]

    # listColumns = ['href','tag', 'brand', 'name','price','specifications']
    listColumns = ['href','tag', 'brand', 'name','price','specifications', 'img_href', 'net_href']
    
    dfGeneral = get_emptyDataframe(listColumns) # Создаём пустой pd.dataframe с столбцами из listColumns

    for zeropage_url in listZeroPages_url:
        soup = get_soup(zeropage_url)
        net_href = get_main_href(zeropage_url) # Получаем "основную" ссылку 
        hrefs = get_hrefs( soup )
        hrefs = list(set(hrefs))
        
    
main()