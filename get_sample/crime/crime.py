import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crime.model.crime_model import CrimeModel
from konlpy.tag import Kkma, Komoran, Okt, Hannanum
from nltk.tokenize import word_tokenize
import konlpy
import nltk
import re 
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud 
import matplotlib.pyplot as plt
import tweepy



class Crime: 

    def __init__(self):
        self.okt = Okt()
        self.data = CrimeModel()
        self.data.dname = 'C:\\Users\\bitcamp\\turingTeam\\chat-server\\get_sample\\crime\\data\\'
        self.data.fname = 'crime_in_seoul.csv'
        self.nouns  =[]
        self.stopwords = []
        self.morpheme =[]

    def preprocessing(self):
        self.okt.pos('삼성전자 글로벌센터 전자사업부', stem=True)
        with open(f'{self.data.dname}{self.data.fname}', 'r',encoding='utf-8') as f:
            texts = f.read()
        texts = texts.replace('\n',' ')          # 줄바꿈 제거
        tokenizer = re.compile(r'[^ㄱ-힣]+')  # 한글만 컴파일
    
        # print(tokenizer.sub(' ' ,texts))
        self.result = tokenizer.sub(' ' ,texts)



    def noun_embedding(self):

        tokens = word_tokenize(self.result)
        for token in tokens:
            pos = self.okt.pos(token)
            _ = [j[0] for j in pos if j[1] == 'Noun']
            if len(''.join(_)) > 1 :
                self.nouns.append(''.join(_))

    
    def stopword_embedding(self):
        self.okt.pos('삼성전자 글로벌센터 전자사업부', stem=True)
        fname = 'stopwords.txt'
        with open(f'{self.data.dname}{fname}', 'r',encoding='utf-8') as f:
            stopwords = f.read()
        self.stopwords = stopwords.split(' ')


    def morpheme_embedding(self):
        print(self.nouns[:10])
        print(self.stopwords[:10])
        self.morpheme = [word for word in self.nouns if word not in self.stopwords]

    def draw_wordcloud(self):
        freqtext = pd.Series(dict(FreqDist(self.morpheme))).sort_values(ascending = False)
        print(freqtext[:10])
        wcloud = WordCloud(font_path = f'{self.data.dname}D2Coding.ttf',
                            relative_scaling=0.2, background_color='white', width=800,height=600).generate_from_frequencies(freqtext)
        plt.figure(figsize=(12,12))
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()


if __name__ == '__main__':
    crime = Crime()
    # nltk.download('punkt')
    crime.preprocessing()
    crime.noun_embedding()
    crime.stopword_embedding()
    crime.morpheme_embedding()
    crime.draw_wordcloud()

