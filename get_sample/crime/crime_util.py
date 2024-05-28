import json
import pandas as pd
from crime.crime_abstract import EditorBase, PrinterBase, ReaderBase, ScraperBase
import googlemaps 
from selenium import webdriver
from icecream import ic

class Printer(PrinterBase):
    def print(self,this:pd.DataFrame) ->None:
        print('*'*100)
        ic(f'타입: {type(this)}')
        ic(f'컬럼: {this.columns}')
        ic(f'상위 1개행 : {this.head(1)}')
        ic(f'null갯수 : {this.isnull().sum()} 개')
        print('*'*100)

class Reader(ReaderBase):
    def __init__(self) -> None:
        pass

    def csv(self,file)->pd.DataFrame:
        return pd.read_csv(f'{file}.csv',encoding='UTF-8', thousands=',')
    
    def excel(self,file,header,usecols)->pd.DataFrame:
        return pd.read_excel(f'{file}.xls',header=header, usecols=usecols,thousands=',')

    def json(self, file) -> pd.DataFrame:
        return json.load(open(f'{file}.json', encoding='UTF-8'))
    
    def gmaps(self,api_key:str) -> pd.DataFrame:
        return googlemaps.Client(key=api_key)


class Scraper(ScraperBase):
    
    def __init__(self)->None:
        pass

    def driver(self) ->object:
        return webdriver.Chrome('C:/Program Files/Google/Chrome/chromedriver.exe')
    

    def auto_login(self, driver, url, selector, data) -> None:
        driver.get(url)
        driver.find_element_by_css_selector(selector).send_keys(data)
        driver.find_element_by_css_selector(selector).submit()


class Editor(EditorBase):
    
    def dropna(self,this: pd.DataFrame)-> pd.DataFrame:
        this.dropna()
        return this