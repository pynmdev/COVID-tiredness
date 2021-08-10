# 이 code 에서 유동인구라 함은 승하차총승객수를 의미한다.

import pandas as pd     # 데이터 처리 lib
import matplotlib.pyplot as plt     # 시각화 lib
import seaborn as sns       # 시각화 lib

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')

# csv 파일 불러오기
file_path_1 = './data/seoul_station_utf8.csv'
raw_data = pd.read_csv(file_path_1, encoding = 'cp949', index_col=False)    # ANSI로 바꿔 저장해서 인코딩 cp949
# print(raw_data.head())
file_path_2 = './data/서울역.csv'   # 이 파일 쓰레기값 들어가 있어서 새로 수정함, 꼭 최신화 할 것
local = pd.read_csv(file_path_2, encoding = 'utf-8', index_col=False)
# print(local.head())
file_path_3 = './data/서울특별시 코로나19 자치구별 확진자 발생동향.csv'
coronic = pd.read_csv(file_path_3, encoding = 'cp949', index_col=False)
# print(coronic.head())
file_path_4 = './data/자치구별 확진자 0727.csv'
coronic_last =  pd.read_csv(file_path_4, encoding = 'utf-8', index_col=False)    # 21/07/27 기준 자치구별 최종 누적 확진자 dataframe
# print(coronic_last.head())


# =============== 여기서 부터는 서울 전체 데이터 작업 ===============
# raw_data 와 coronic 에서 날짜형식 통일하기
raw_data["사용일자"] = pd.to_datetime(raw_data["사용일자"], format='%Y%m%d')
# print(raw_data.head())
coronic["자치구 기준일"] = coronic["자치구 기준일"].str.slice(start=0 , stop=10)    # 앞에서부터 10글자 가져온다
coronic["자치구 기준일"] = pd.to_datetime(coronic["자치구 기준일"], format='%Y.%m.%d')      # Y 2021 y 21 . 구분자
# print(coronic.head())

# coronic 에서 일자별로 기타 추가 column 가져오기
pd.set_option('mode.chained_assignment', None)     # ↓자꾸 에러떠서 경고문 끔
coronic = coronic.sort_values(by=['자치구 기준일'])   # 기준일자로 sorting
coronic_new = coronic.filter(regex='기준일|추가')    # '기준일' 이라는 string 들어간 열, '추가'라는 string 들어간 열 filtering
# coronic_new = coronic.filter(regex='기준일|전체')      # 전체 누적 확진자를 확인하려면 이 코드 쓰기
coronic_new['일일 신규확진자수'] = coronic_new.iloc[:, 1:26].sum(axis=1)      # 1~26 열 합계
coronic_new = coronic_new[['자치구 기준일', '일일 신규확진자수']]
# print(coronic_new.head())

# raw_data 에서 일자별로 유동인구 sum 하기
raw_data_sum = raw_data.groupby(['사용일자'], as_index=False)['승하차총승객수'].sum()
# print(raw_data_sum)

# raw_data_sum 과 coronic merge 하기
# coronic_new dataframe 의 column 명 바꾸기(자치구 기준일->사용일자)
coronic_new.rename(columns={'자치구 기준일':'사용일자'}, inplace = True)
add_coronic_new = pd.merge(raw_data_sum, coronic_new, how='inner', on='사용일자')   # 날짜 앞뒤로 어긋나서 inner join
print("**********서울시 일별 유동인구-확진자 상관관계**********")
print(add_coronic_new)

# 시각화 (선 그래프 형식, x축 날짜, y1축 유동인구, y2축 일별 확진자)
draw1 = sns.lineplot(x='사용일자',
                  y='승하차총승객수',
                  data=add_coronic_new,
                  color='blue')
draw2 = draw1.twinx()   # 두 그래프 합치기
draw2 = sns.lineplot(x='사용일자',
                  y='일일 신규확진자수',
                  data=add_coronic_new,
                  color='red')
plt.show()  # 실제 그래프 출력
plt.savefig('./1.png')

# =============== 여기서 부터는 자치구별 데이터 작업 ===============

# 원본 파일에 자치구 column 추가하기
add_local = pd.merge(raw_data, local, how='left', on='역명')      # 역명을 기준으로 raw_data 에 left join 하겠다
# print(add_local)

# 자치구 column 추가된 dataframe 에서 3개(일자, 자치구, 유동인구) column 만 추출하기
select_col = add_local[['사용일자', '승하차총승객수', '자치구']]      # TODO 왜 []가 하나 더 필요한지 찾아보기
# print(select_col)

# TODO 데이터프레임 엑셀로 저장하기
# 중요한건 아니라 일단 pass

# 자치구 별로 승하차총승객수 합치기
select_col = select_col.groupby(['자치구'], as_index=False)['승하차총승객수'].sum()       # 자치구 별로 그룹짓고 유동인구 합치기
# print(select_col)

# 자치구 column 추가된 dataframe 에서 확진자 수 column 추가하기
# merge 이전에 sort 로 전처리
select_col = select_col.sort_values(by='자치구', ascending=True)
coronic_last = coronic_last.sort_values(by='자치구', ascending=True)
# print(select_col)
# print(coronic_last)
# print(select_col.dtypes)
# print(coronic_last.dtypes)

# coronic_last dataframe 에서 index 남아 있어서 reset 해주려 했으나 이걸 포함시키면 index column 이 생기는 문제 발생
# coronic_last = coronic_last.reset_index()

# 실제로 column 추가
add_coronic_last = pd.merge(select_col, coronic_last, how='left', on='자치구')
print("**********자치구별 유동인구-확진자 상관관계**********")
print(add_coronic_last)

# TODO x축 scale 수정하기, 점 설명탭 size 줄이기
# 자치구별 시각화(유동인구-확진자 산점도 그래프)
sns.scatterplot(x='승하차총승객수', y='확진자 수', hue='자치구', data=add_coronic_last)        # hue는 점마다 색 입혀서 자치구 구분하는 옵션
plt.legend(loc='upper right', bbox_to_anchor=(1, 1), ncol=1)
plt.show()      # 그래프 출력
plt.savefig('./2.png')

# =============== 여기서 부터는 상관관계 회귀분석 ===============
# sns.set_style("darkgrid")
sns.lmplot(x='승하차총승객수', y='확진자 수', data=add_coronic_last, height=8, scatter_kws={'color': 'red'}, line_kws={'color': 'red'})
plt.title("상관관계 분석", size=15)
plt.show()
plt.savefig('./3.png')

# =============== 여기서 부터는 지도 그리기 ===============
import json
import folium
geo_path = './data/skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))

seoul_map = folium.Map(location=[37.5502, 126.982], zoom_start=10.5, titles='cartodbpositron')
seoul_map.choropleth(geo_data=geo_str,
                     data=add_coronic_last,
                     columns=['자치구', '승하차총승객수'],
                     fill_color='YlGn',      #RdPu, OrRd, YlOrRd
                     key_on='feature.properties.name',
                     highlight=True,
                     fill_opacity=0.5, line_opacity=1,
                     legend_name='population(people)')
seoul_map.save('seoul_map.html')
seoul_map