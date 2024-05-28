import os
import sys

import numpy as np
from sklearn import preprocessing
sys.path.append(os.path.dirname(os.path.dirname((os.path.dirname(os.path.abspath(__file__))))))
import folium
import googlemaps
from dotenv import load_dotenv

from crime.crime_util import Editor, Reader
from crime.model.crime_model import CrimeModel
from icecream import ic
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, ".env"))

'''
문제정의 !
서울시의 범죄현황과 CCTV현황을 분석해서
정해진 예산안에서 구별로 다음해에 배분하는 기준을 마련하시오.
예산금액을 입력하면, 구당 할당되는 CCTV 카운터를 자동으로
알려주는 AI 프로그램을 작성하시오.
'''

class CrimeService:
    
    def __init__(self):
        self.data = CrimeModel()
        self.reader = Reader()
        self.editor = Editor()
        this = self.data
        this.dname = 'C:\\Users\\bitcamp\\turingTeam\\chat-server\\get_sample\\crime\\data\\'
        this.sname = 'C:\\Users\\bitcamp\\turingTeam\\chat-server\\get_sample\\crime\\save\\'
        this.crime = 'crime_in_seoul.csv'
        this.cctv = 'cctv_in_seoul.csv'
        self.crime_rate_columns = ['살인검거율','강도검거율','강간검거율','절도검거율','폭력검거율']
        self.crime_columns = ['살인','강도','강간','절도','폭력']
        self.arrest_columns = ['살인 검거','강도 검거','강간 검거','절도 검거','폭력 검거']

    

    def new_dataframe(self, dname:str, fname: str) -> pd.DataFrame:
        this = self.data
        # index_col=0 해야 기존 index 값이 유지된다. 
        # 0은 컬럼명 중에서 첫번째를 의미한다.(배열구조)
        # pd.read_csv(f'경로/파일명/csv',index_col=0 => 인덱스로 지정할 column 명) index 지정
        return pd.read_csv(f'{dname}{fname}',encoding='UTF-8', thousands=',')
    

   
    def save_model(self, fname, dframe: pd.DataFrame) -> pd.DataFrame:
        this =self.data
        '''
        풀옵션은 다음과 같다
        df.to_csv(f'{self.ds.sname}{fname}',sep=',',na_rep='NaN',
                         float_format='%.2f',  # 2 decimal places
                         columns=['ID', 'X2'],  # columns to write
                         index=False)  # do not write index
        '''
        return dframe.to_csv(f'{this.sname}{fname}',sep=',',na_rep='NaN') 


    def save_police_position(self) ->None:
        station_names = []
        crime = self.new_dataframe(self.data.dname,self.data.crime)
        for name in crime['관서명']:
            station_names.append('서울'+str(name[:-1])+'경찰서')
        ic(station_names)
        station_address = []
        station_lats =[]
        station_lngs =[]
        
        gmaps = self.reader.gmaps(os.environ["api_key"])
        for name in station_names:
            t = gmaps.geocode(name,language ='ko')
            print(t)
            station_address.append(t[0].get("formatted_address"))
            t_loc = t[0].get("geometry")
            station_lats.append(t_loc['location']['lat'])
            station_lngs.append(t_loc['location']['lng'])


        # gmaps = self.reader.gmaps(os.environ["api_key"])
        # stations = pd.DataFrame(columns=['경찰서명', '위도', '경도', '구별'])

        # stations['경찰서명'] = [ '서울' + str(name[:-1]) + '경찰서' for name in crime['관서명']]
        
        # for i in range(len(stations['경찰서명'])):
        #     tmpMap = gmaps.geocode(stations['경찰서명'][i], language='ko')
        #     station_addrs = tmpMap[0].get('geometry')
        #     stations['위도'][i] = station_addrs['location']['lat']
        #     stations['경도'][i] = station_addrs['location']['lng']
        #     stations['구별'][i] = [gu['short_name'] for gu in tmpMap[0]['address_components'] if gu['short_name'][-1] == '구'][0]
        gu_names = []
        for name in station_address:
            tmp = name.split()
            gu_name = [gu for gu in tmp if gu[-1] == '구'][0]
            gu_names.append(gu_name)

        crime['구별'] = gu_names
        # 구와 경찰서의 위치가 다른경우 수작업
        crime.loc[crime['관서명'] == '혜화서',['구별']] = '종로구'
        crime.loc[crime['관서명'] == '서부서',['구별']] = '은평구'
        crime.loc[crime['관서명'] == '강서서',['구별']] = '강서구'
        crime.loc[crime['관서명'] == '종암서',['구별']] = '성북구'
        crime.loc[crime['관서명'] == '방배서',['구별']] = '서초구'
        crime.loc[crime['관서명'] == '수서서',['구별']] = '강남구'
        crime.loc[crime['관서명'] == '혜화서',['구별']] = '종로구'

        crime.to_csv(f'{self.data.sname}police_position.csv')


    def save_cctv_population(self) -> None:
        usecols= ['자치구','합계','한국인','등록외국인','65세이상고령자']
        # population = self.reader.excel(f'{self.data.dname}pop_in_seoul',1,usecols)
        population = self.reader.excel(f'{self.data.dname}pop_in_seoul', 2,'B,D,G,J,N')
        cctv = self.new_dataframe(self.data.dname,self.data.cctv)
        cctv.rename(columns={cctv.columns[0]: '구별'}, inplace=True)
        population.rename(columns={population.columns[0]: '구별',
                                   population.columns[1]: '인구수',
                                   population.columns[2]: '한국인',
                                   population.columns[3]: '외국인',
                                   population.columns[4]: '고령자',
                                   },inplace=True)
        # ic(population.head(2))
        # ic(cctv.head(2))
        #population 에서 NaN있는지 확인후 제거
        # population = self.editor.dropna(population)
        # population.dropna(how='all',inplace=True) # NaN 값제거 
        population.drop(26, axis=0,inplace=True) #26번째 행 제거 , axis=0은 행을 삭제 axis=1 열을 삭제 
        population['외국인비율'] = population['외국인'].astype(int) / population['인구수'].astype(int) *100
        population['고령자비율'] = population['고령자'].astype(int) / population['인구수'].astype(int) *100
        cctv.drop(['2013년도 이전', '2014년','2015년','2016년'], axis=1,inplace=True)
        cctv_per_populations = pd.merge(cctv,population,on="구별")
        ic(cctv_per_populations)
        cor1 = np.corrcoef(cctv_per_populations['고령자비율'],cctv_per_populations['소계'])
        cor2 = np.corrcoef(cctv_per_populations['외국인비율'],cctv_per_populations['소계'])
        # ic(f'고령자 비율과 cctv 상관계수 {str(cor1)} \n'
        #     f'외국인비율과 cctv 상관계수 {str(cor2)}')
        
        """
         고령자비율과 CCTV 의 상관계수 [[ 1.         -0.28078554]
                                     [-0.28078554  1.        ]] 
         외국인비율과 CCTV 의 상관계수 [[ 1.         -0.13607433]
                                     [-0.13607433  1.        ]]
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계                       
         """
        cctv_per_populations.to_csv(f'{self.data.sname}cctv_per_populations.csv')
        
        
    def save_crime_arrest_normaliztion(self)-> None:
        '''범죄건수와 cctv와의 상관관계.
        검거율과 cctv와의 상관관계.'''
        police_position = self.new_dataframe(self.data.sname,'police_position.csv')
        cctv = self.new_dataframe(self.data.dname,self.data.cctv)
        police = pd.pivot_table(police_position, index='구별',aggfunc=np.sum)
        police.rename(columns={'강간 발생' : '강간',
                               '강도 발생' : '강도',
                               '살인 발생' : '살인',
                               '절도 발생' : '절도',
                               '폭력 발생' : '폭력',
                               },inplace=True)
        
        police['살인검거율'] = police['살인 검거'].astype(int) / police['살인'].astype(int) *100
        police['강도검거율'] = police['강도 검거'].astype(int) / police['강도'].astype(int) *100
        police['강간검거율'] = police['강간 검거'].astype(int) / police['강간'].astype(int) *100
        police['절도검거율'] = police['절도 검거'].astype(int) / police['절도'].astype(int) *100
        police['폭력검거율'] = police['폭력 검거'].astype(int) / police['폭력'].astype(int) *100

        for i in self.crime_rate_columns:
            police.loc[police[i]>100,i] =100

        police.drop(['살인 검거','강도 검거','강간 검거','절도 검거','폭력 검거'],axis=1,inplace=True)
        
        print('loc 결과 : ')
        
        x = police[self.crime_rate_columns].values
        
        min_max_scalar = preprocessing.MinMaxScaler()
        """
        피쳐 스케일링(Feature scalining)은 해당 피쳐들의 값을 일정한 수준으로 맞춰주는 것이다.
        이때 적용되는 스케일링 방법이 표준화(standardization) 와 정규화(normalization)다.
        
        1단계: 표준화(공통 척도)를 진행한다.
            표준화는 정규분포를 데이터의 평균을 0, 분산이 1인 표준정규분포로 만드는 것이다.
            x = (x - mu) / sigma
            scale = (x - np.mean(x, axis=0)) / np.std(x, axis=0)
        2단계: 이상치 발견 및 제거
        3단계: 정규화(공통 간격)를 진행한다.
            정규화에는 평균 정규화, 최소-최대 정규화, 분위수 정규화가 있다.
             * 최소최대 정규화는 모든 데이터를 최대값을 1, 최솟값을 0으로 만드는 것이다.
            도메인은 데이터의 범위이다.
            스케일은 데이터의 분포이다.
            목적은 도메인을 일치시키거나 스케일을 유사하게 만든다.     
        """
        x_scaled = min_max_scalar.fit_transform(x.astype(int))
        ic(x_scaled)
        police_norm = pd.DataFrame(x_scaled,columns=self.crime_rate_columns,index=police.index)
        ic(police_norm)
        police_norm[self.crime_columns] = police[self.crime_columns]
        police_norm['범죄'] = np.sum(police_norm[self.crime_rate_columns],axis=1)
        police_norm['검거'] = np.sum(police_norm[self.crime_columns],axis=1)
        police_norm.to_csv(f'{self.data.sname}police_norm.csv',sep=',',encoding='UTF-8')
        # crime.drop(['관서명','Unnamed: 0'],axis=1,inplace=True)
     
        # crime['발생합계'] = crime['살인 발생'].astype(int)+crime['강도 발생'].astype(int)+crime['강간 발생'].astype(int)+crime['절도 발생'].astype(int)+crime['폭력 발생'].astype(int)
        # crime['검거합계'] = crime['살인 검거'].astype(int)+crime['강도 검거'].astype(int)+crime['강간 검거'].astype(int)+crime['절도 검거'].astype(int)+crime['폭력 검거'].astype(int)
        
        # # crime['살인발생율'] = crime['살인 발생'].astype(int) / crime['발생합계'].astype(int) *100
        # # crime['강도발생율'] = crime['강도 발생'].astype(int) / crime['발생합계'].astype(int) *100
        # # crime['강간발생율'] = crime['강간 발생'].astype(int) / crime['발생합계'].astype(int) *100
        # # crime['절도발생율'] = crime['절도 발생'].astype(int) / crime['발생합계'].astype(int) *100
        # # crime['폭력발생율'] = crime['폭력 발생'].astype(int) / crime['발생합계'].astype(int) *100
        
        # crime.drop(['살인 검거','강도 검거','강간 검거','절도 검거','폭력 검거','살인 발생','강도 발생','강간 발생','절도 발생','폭력 발생'],axis=1,inplace=True)
        # cctv.drop(['2013년도 이전', '2014년','2015년','2016년'], axis=1,inplace=True)
        # cctv.rename(columns={cctv.columns[0]: '구별'}, inplace=True)

        # cctv_per_crime = pd.merge(cctv,crime,on="구별")

        # cor1 = np.corrcoef(cctv_per_crime['발생합계'],cctv_per_crime['소계'])
        # cor2 = np.corrcoef(cctv_per_crime['검거합계'],cctv_per_crime['소계'])
        # ic(f'발생합계와 cctv 상관계수 {str(cor1)} \n'
        #     f'검거합계와 cctv 상관계수 {str(cor2)}')
        # ic(cctv_per_crime)
        
        # cctv_per_crime.to_csv(f'{self.data.sname}cctv_per_crime.csv')


    def folium_test(self):
        state_geo = self.reader.json(f'{self.data.dname}us-states')
        state_data = self.reader.csv(f'{self.data.dname}us_unemployment')
        m = folium.Map(location=[48, -102], zoom_start=3)
        folium.Choropleth(
            geo_data=state_geo,
            name="choropleth",
            data=state_data,
            columns=["State", "Unemployment"],
            key_on="feature.id",
            fill_color="YlGn",
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name="Unemployment Rate (%)",
        ).add_to(m)

        folium.LayerControl().add_to(m)
        m.save(f'{self.data.sname}us_states.html')
        
    def draw_crime_map(self):
        state_geo = self.reader.json(f'{self.data.dname}kr-states')
        police_norm = self.reader.csv(f'{self.data.sname}police_norm')
        police_position = self.reader.csv(f'{self.data.sname}police_position')

        m = folium.Map(location=[37.5502, 126.982], zoom_start=12, title='Stamen Toner')
        crime = self.new_dataframe(self.data.dname,self.data.crime)
        station_names = []
        for name in crime['관서명']:
            station_names.append('서울' + str(name[:-1]) + '경찰서')
        station_addreess = []
        station_lats = []
        station_lngs = []
        gmaps = self.reader.gmaps(os.environ["api_key"])
        for name in station_names:
            t= gmaps.geocode(name, language='ko')
            station_addreess.append(t[0].get("formatted_address"))

            t_loc = t[0].get("geometry")
            station_lats.append(t_loc['location']['lat'])
            station_lngs.append(t_loc['location']['lng'])
        police_position['lat'] = station_lats
        police_position['lng'] = station_lngs

        temp = police_position[self.arrest_columns] / police_position[self.arrest_columns].max()
        
        police_position['검거' ] = np.sum(temp, axis=1)
        
        folium.Choropleth(
            geo_data=state_geo,
            name="choropleth",
            data=tuple(zip(police_norm['구별'], police_norm['범죄'])),
            columns=["State", "Crime Rate"],
            key_on="feature.id",
            fill_color="PuRd",
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name="Crime Rate (%)",
        ).add_to(m)
        for i in police_position.index:
            folium.CircleMarker([police_position['lat'][i], police_position['lng'][i]],
                                radius=police_position['검거'][i]*10,
                                fill_color='#0a0a32').add_to(m)
        folium.LayerControl().add_to(m)
        m.save(f'{self.data.sname}kr_states.html')
        


if __name__ == '__main__':
    main = CrimeService()
    # ic(main.new_dataframe(main.data.crime))
    # main.save_police_position()
    # ic(main.new_dataframe(main.data.cctv))
    # print('='*50)
    # main.save_cctv_population()
    # main.save_crime_arrest_normaliztion()
    main.draw_crime_map()
    