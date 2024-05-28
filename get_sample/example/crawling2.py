

from urllib.request import urlopen

from bs4 import BeautifulSoup


class ScrapBug():

    def scrap(self) -> {}:
        print('벅스뮤직사이트에서 데이터 수집')
        url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc,'lxml')
        list1 = self.find_music(soup,'title')
        list2 = self.find_music(soup,'artist')
        a = [i if i ==0 or i ==0 else i for i in range(1)]
        b = [i if i ==0 or i ==0 else i for i in []]
        c = [(i,j) for i, j in enumerate([])]
        d = {i : j for i, j in zip(list1,list2)}
        l = [i + j for i,j in zip(list1,list2)]
        l2 = list(zip(list1,list2))
        d1 = dict(zip(list1,list2))
        print(d1)
        return d 
    
    @staticmethod
    def find_music(soup:BeautifulSoup,classname :str):
        list =soup.find_all('p',{'class':classname})
        return [i.get_text() for i in list]
    
if __name__ == '__main__':
    bugs = ScrapBug()
    bugs.scrap()