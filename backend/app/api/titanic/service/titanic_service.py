
from xarray import Dataset
from app.api.titanic.model.titanic_model import TitanicModel
import pandas as pd 
import numpy as np

class TitanicService:

    model = TitanicModel()

    def preprocess(self) :
        
        print(f'전처리 시작')
     
        self.model.preprocess('train.csv', 'test.csv')
        

    def modeling(self):

        print(f'모델링 시작')
        
        this = self.model
    
    def learning(self):
        print(f'학습 시작')
        print(f'결정트리를 활용한 검증 정확도 : ')
        print(f'랜덤프레스트를 활용한 검증 정확도 : ')
        print(f'나이브베이즈를 활용한 검증 정확도 : ')
        print(f'KNN를 활용한 검증 정확도 : ')
        print(f'SVN를 활용한 검증 정확도 : ')
        this = self.model

    def postprocessing(self):
        
        print(f'후처리 시작')
        
        this = self.model

    def submit(self):
        
        print(f'제출 시작')
        
        this = self.model