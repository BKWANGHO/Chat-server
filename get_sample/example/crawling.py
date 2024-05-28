from bs4 import BeautifulSoup
import requests

class BugsMusic(object):

    def __init__(self) -> None:
        self.url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.class_name = []
        self.title_list = []
        self.artist_list = []
        self.dict = {}


    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text


    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        pass


    def insert_title_dict(self):
        # 방법 1. range
        for i in range(0, len(self.title_list)):
            pass
        # 방법 2. zip
        for i, j in zip(self.title_list, self.artist_list):
            pass
        # 방법 3. enumerate
        for i, j in enumerate(self.title_list):
            pass


        print(dict)




if __name__ == "__main__":
    bugs = BugsMusic()
    while 1:
        menu = input('0-exit, 1-input time, 2-output, 3-print dict')
        if menu == '0':
            break
        elif menu == '1':
            bugs.set_url('wl_ref=M_contents_03_01')
        elif menu == '2':
            bugs.class_name.append("artist")
            bugs.class_name.append("title")
            bugs.get_ranking()
        elif menu == '3':
            bugs.insert_title_dict()
        else:
            print('Wrong Number')
            continue