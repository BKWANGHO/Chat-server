from context.model.data_model import DataModel
import pandas as pd


class DataService:
    def __init__(self):
        self.data = DataModel()
        this = self.data
        this.dname = './data/'
        this.sname = './save/'

    def get_sname(self):
        return self.data.sname

    def new_dframe_idx(self, fname: str) -> object:
        this = self.data
        # index_col=0 해야 기존 index 값이 유지된다
        # 0은 컬럼명 중 첫번째를 의미한다(배열구조)
        # pd.read_csv('경로/파일명.csv', index_col = '인덱스로 지정할 column명') Index 지정
        return pd.read_csv(f'{this.dname}{fname}', index_col=0)

    def new_dframe(self, fname: str) -> object:
        this = self.data
        # pd.read_csv('경로/파일명.csv') Index 지정하지 않음
        return pd.read_csv(f'{this.dname}{fname}')

    def save_model(self, fname: str, dframe: pd.DataFrame):
        this = self.data
        '''
        풀옵션은 다음과 같다
        df.to_csv(f'{self.data.sname}{fname}',sep=',',na_rep='NaN',
                         float_format='%.2f',  # 2 decimal places
                         columns=['ID', 'X2'],  # columns to write
                         index=False)  # do not write index
         '''
        dframe.to_csv(f'{this.sname}{fname}', sep=',', na_rep='NaN')