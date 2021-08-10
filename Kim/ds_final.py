# -*- coding: utf-8 -*-
# %%
import pandas as pd
from statistics import mean
import matplotlib.pyplot as plt # 막대그래프
from matplotlib import rcParams , font_manager, rc
import matplotlib
matplotlib.font_manager._rebuild()
#한글깨짐 폰트설정
font_path = 'C:\\Users\\ksy\\Downloads\\MaruBuri-Regular\\MaruBuri-Regular.ttf'
font = font_manager.FontProperties(fname=font_path, size=18).get_name()
rc('font' , family = font)
plt.rcParams['axes.unicode_minus'] = False #한글 폰트 사용시 마이너스 폰트 깨짐 해결

def subway_st(all_data):
    pdata = all_data
    seoul_station = ["가락시장","가산디지털단지","가양","가오리",	"가좌",	"강남",	"강남구청",	"강동",	"강동구청",	"강변",	"강일",	"개롱",	"개봉",	"개포동",	"개화",	"개화산",	"거여",	"건대입구",	"경복궁",	"경찰병원",	"고덕",	"고려대",	"고속터미널",	"공덕",	"공릉",	"공항시장",	"광나루",	"광운대",	"광화문",	"광흥창",	"교대",	"구로",	"구로디지털단지",	"구룡",	"구반포",	"구산",	"구의",	"구일",	"구파발",	"국회의사당",	"군자",	"굽은다리",	"금천구청",	"금호",	"길동",	"길음",	"김포공항",	"까치산",	"낙성대",	"남구로",	"남부터미널",	"남성",	"남영",	"남태령",	"내방",	"노들",	"노량진",	"노원",	"녹번",	"녹사평",	"녹천",	"논현",	"답십리",	"당고개",	"당산",	"대림",	"대모산입구",	"대방",	"대청",	"대치",	"대흥",	"도곡",	"도림천",	"도봉",	"도봉산",	"독립문",	"독바위",	"독산",	"돌곶이",	"동대문",	"동대문역사문화공원",	"동대입구",	"동묘앞",	"동작",	"둔촌동",	"둔촌오륜",	"등촌",	"디지털미디어시티",	"뚝섬",	"뚝섬유원지",	"마곡",	"마곡나루",	"마들",	"마장",	"마천",	"마포",	"마포구청",	"망우",	"망원",	"매봉",	"먹골",	"면목",	"명동",	"명일",	"목동",	"몽촌토성",	"무악재",	"문래",	"문정",	"미아",	"미아사거리",	"반포",	"발산",	"방배",	"방이",	"방학",	"방화",	"버티고개",	"보라매",	"보문",	"복정",	"봉은사",	"봉천",	"봉화산",	"북한산보국문",	"북한산우이",	"불광",	"사가정",	"사당",	"사평",	"삼각지",	"삼성",	"삼성중앙",	"삼양",	"삼양사거리",	"삼전",	"상계",	"상도",	"상봉",	"상수",	"상왕십리",	"상월곡",	"상일동",	"새절",	"샛강",	"서강대",	"서대문",	"서빙고",	"서울대입구",	"서울숲",	"서울역",	"서초",	"석계",	"석촌",	"석촌고분",	"선릉",	"선유도",	"선정릉",	"성수",	"성신여대입구",	"솔샘",	"솔밭공원",	"송정",	"송파",	"송파나루",	"수락산",	"수색",	"수서",	"수유",	"숙대입구",	"숭실대입구",	"시청",	"신금호",	"신길",	"신내",	"신논현",	"신답",	"신당",	"신대방",	"신대방삼거리",	"신도림",	"신림",	"신목동",	"신반포",	"신방화",	"신사",	"신설동",	"신용산",	"신이문",	"신정",	"신정네거리",	"신촌(2)",	"신촌(경)",	"신풍",	"쌍문",	"아차산",	"아현",	"안국",	"안암",	"암사",	"압구정",	"압구정로데오",	"애오개",	"약수",	"양원",	"양재",	"양재시민의숲",	"양천구청",	"양천향교",	"양평(5)",	"어린이대공원",	"언주",	"여의나루",	"여의도",	"역삼",	"역촌",	"연신내",	"염창",	"영등포",	"영등포구청",	"영등포시장",	"오금",	"오류동",	"오목교",	"옥수",	"온수",	"올림픽공원",	"왕십리",	"외대앞",	"용답",	"용두",	"용마산",	"용산",	"우장산",	"월계",	"월곡",	"월드컵경기장",	"을지로입구",	"을지로3가",	"을지로4가",	"응봉",	"응암",	"이대",	"이수",	"이촌",	"이태원",	"일원",	"잠실",	"잠실나루",	"잠실새내",	"잠원",	"장승배기",	"장지",	"장한평",	"정릉",	"제기동",	"종각",	"종로3가",	"종로5가",	"종합운동장",	"중계",	"중곡",	"중랑",	"중앙보훈병원",	"중화",	"증미",	"증산",	"창동",	"창신",	"천왕",	"천호",	"청구",	"청담",	"청량리",	"충무로",	"충정로",	"태릉입구",	"하계",	"학동",	"학여울",	"한강진",	"한남",	"한성대입구",	"한성백제",	"한양대",	"한티",	"합정",	"행당",	"혜화",	"홍대입구",	"홍제",	"화계",	"화곡",	"화랑대",	"회기",	"회현",	"효창공원앞",	"흑석"	]
    station = pdata["역명"].unique()

    cnt =0
    same_st = []
    for j in seoul_station: # 여기서 단어를 비교
        for i in station:   # statiion 내부 값에 () 가 추가로 붙어있음
            #print(j.find(i))
            if i.find(j) >= 0 and i not in same_st:
                if i==j:
                    same_st.append(i)
                elif i.find(j+"(")==0:
                    same_st.append(i)   
            elif i == "신촌" and j == "신촌(2)":
                same_st.append(j)
            elif i == "신촌" and j == "신촌(경)":
                same_st.append(j)
            elif i == "양평" and j == "양평(5)":
                same_st.append(j)

    seoul_data = all_data[ all_data["역명"].isin(same_st) ]
    #print(seoul_data) # 위의 신촌 2개 양평 1개가 빠진 데이터 채워넣으면 된다.
    return seoul_data

from glob import glob # 파일 경로를 조작할 수 있다.
import chardet
def subway_all_file():
    file_path = glob('C:\\Users\\ksy\\downloads\\data\\*.csv')
    all_file = []
    #print(file_path)
    #인코딩 확인 코드-----------------------------------------------
    for path in file_path:
        rawdata = open(path, 'rb').read() #파일 열고
        result = chardet.detect(rawdata) # 인코딩 형식 검사하고
        charenc = result['encoding']  # 인코딩 결과 확인하고
    #인코딩 확인 코드 마무리 ----------------------------------------
        csvfile = pd.read_csv(path ,encoding = charenc , index_col=False)
        all_file.append(csvfile)
    all_data = pd.concat(all_file, ignore_index=True)
    all_data["사용일자"] = pd.to_datetime(all_data["사용일자"], format='%Y%m%d')

    # 이제 모아놓은 전 엑셀 데이터를 서울을 주소지로 갖는 역으로 필터링 해주어야 한다.
    all_data = subway_st(all_data)
#--시각화 진행 함수로 만들기도 가능----------------------------------------------------------------------------------
    subway_col = [i for i in all_data.columns]

    all_data["승하차총승객수"] = all_data["승차총승객수"] + all_data["하차총승객수"]
#----------------------------선그래프----------------------
    #plt.plot(pdata_sum["사용일자"] , pdata_sum["승하차총승객수"])
    #plt.show()
#----------------------------막대그래프----------------------
    #plt.bar(pdata_sum["사용일자"] , pdata_sum["승하차총승객수"])
    #plt.show()
    print('-----------------------------------------------------------')
    return all_data #잠깐 all_data 사용중 원래 pdata_sum 리턴

def geori_index(georidoogi_start, georidoogi_end , pdata_sum , georidoogi_gov_summa):
    # 비교위해 리스트 datetime 으로 변환 
    georidoogi_start = pd.to_datetime(georidoogi_start , format = '%Y.%m.%d')
    georidoogi_end = pd.to_datetime(georidoogi_end , format = '%Y.%m.%d')
    pdata_sum_add_dangye = pdata_sum
    # pdata_sum 내부에 날짜의 index를 담기위함
    temp_start = []
    temp_end = []
    for idx , i in enumerate(pdata_sum['사용일자']): # i가 날짜들 
        for j in georidoogi_start:
            if i == j:
                temp_start.append(idx)
        for k in georidoogi_end:
            if i ==k and idx: # not in temp_end
                temp_end.append(idx)
            if i.year == 2021 and i.month == 7 and i.day == 27:
                if idx not in temp_end:
                    temp_end.append(idx)

    for i in range(0, len(temp_start)):
        pdata_sum_add_dangye.loc[temp_start[i]:temp_end[i] , "dangye"] = georidoogi_gov_summa[i]

    return temp_start , temp_end , pdata_sum_add_dangye

from matplotlib import colors as mcolors
import plotly
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from plotly import tools
import seaborn as sns
def gu_corona():
    file_path = 'C:\\Users\\ksy\\downloads\\서울특별시 코로나19 자치구별 확진자 발생동향.csv'
    pdata = pd.read_csv(file_path , encoding ='cp949' , index_col=False)
    #뒤에 분초를 떼어버렸다.
    pdata["자치구 기준일"] = pdata["자치구 기준일"].str.slice(start=0 , stop=10)
    pdata["자치구 기준일"] = pd.to_datetime(pdata["자치구 기준일"] , format = '%Y.%m.%d')
    # 날짜기준 정렬
    pdata = pdata.sort_values(by = ['자치구 기준일'])  
#--------------------------------------------------------------------
    # 자치구별 신규확진자수 추출해 데이터프레임생성 -------------------
    new = pdata.filter(regex='기준일|추가') # 아래랑 주석 바꾸려면 밑에 수치부분도 주석풀기
    #new = pdata.filter(regex='기준일|전체')
    new['총신규확진자수'] = new.iloc[:,1:26].sum(axis=1)
    new = new[['자치구 기준일' , '총신규확진자수']]
#--------------------------------------------------------------------
    #거리두기 단계별 시작과 끝 담기
    # df = pdata_all.sort_values(by = ['확진자수'], ascending = False)       
                        #  거리두기    강화된거리두기     일부 조치완화    생활거리두기    3단계거리두기   3단계거리두기   4단계거리두기  4단계거리두기  4단계거리두기   4단계거리두기       5단계         5단계         특별대책      특별대책            
    georidoogi_start =  ['2020-02-29' , '2020-03-22' , '2020-04-20' , '2020-05-06' , '2020-06-28' , '2020-08-16', '2020-08-30' , '2020-09-14' , '2020-09-28' ,  '2020-10-12' , '2020-11-19', '2020-12-08', '2020-12-23', '2021-01-16', '2021-02-06', '2021-02-15', '2021-07-12']
    georidoogi_end =    ['2020-03-21' , '2020-04-19' , '2020-05-05' , '2020-06-27' , '2020-08-15' , '2020-08-29' , '2020-09-13', '2021-09-27' , '2020-10-11' ,  '2020-11-18' , '2020-12-07', '2020-12-22', '2021-01-15', '2021-02-05', '2021-02-14', '2021-07-11', '2021-07-27'] # 8.8까지지만 자료가 7.27이 끝이므로
    georidoogi_gov = [ '거리두기'  , '강화된거리두기' ,'일부 조치완화','생활거리두기', '3단계거리두기' , '3단계거리두기','4단계거리두기','4단계거리두기', '4단계거리두기','4단계거리두기','5단계거리두기','5단계거리두기','특별대책'   ,'특별대책' ,   '특별대책',   '추가조치',   '추가조치']
    georidoogi_gov_summa = ['2단계' ,    '2.5단계',       '2단계',        '1단계',      '1단계'       , '2단계'  ,     '2.5단계',    '2단계',       '2.5단계',       '1단계',       '1.5단계',    '2.5단계',    '2.5+단계',    '2.5-단계',  '2.5--단계',    '2단계',    '4+단계']
    print( len(georidoogi_start) , len(georidoogi_end) , len(georidoogi_gov_summa))
    
    # 서울시 내로 분류된 서울 승하차인원 데이터
    all_data = subway_all_file()
    pdata_sum = all_data.groupby(['사용일자'], as_index = False)["승하차총승객수"].sum()

    new.rename(columns = {'자치구 기준일' : '사용일자'}, inplace = True)
    pdata_sum = pd.merge( new ,pdata_sum, how='left', on='사용일자' )
    pdata_sum['총신규확진자수'] = pdata_sum['총신규확진자수'].values * 12000  # 추가확진자(신규확진자)
    # pdata_sum['총신규확진자수'] = pdata_sum['총신규확진자수'].values * 180 # 누적확진자수그래프           
    print(pdata_sum)

    # 서울승하차인원데이터에서 거리두기 날짜와 일치하는 index
    temp_start , temp_end , temp_dangye = geori_index(georidoogi_start , georidoogi_end , pdata_sum , georidoogi_gov_summa)
    print("거리두기 정책 시작일 " ,len(temp_start) ,  temp_start) #실제 index 가 담겨있다.
    print("거리두기 정책 종료일 " ,len(temp_end) , temp_end)
    print(temp_dangye)

    pdata = pdata.transpose()
    pdata.rename(columns = pdata.iloc[0] , inplace=True)
    pdata = pdata.drop(pdata.index[0])
    pdata_add = pdata[1::2]
    pdata_all = pdata[0:-1:2]
    print('--------------pdata_all')
    print(pdata_all)

    pdata_all_x = pdata.columns.to_list()
    pdata_all_y = pdata_all.loc[pdata_all.index[0]].to_list()

    pdata_sum_x = pdata_sum['사용일자'].to_list()
    pdata_sum_y = pdata_sum['승하차총승객수'].to_list()
    print("pdata_sum_x 의 개수는 " , len(pdata_sum_x))
    
    #clr_list = ['aqua','deepskyblue','peru','orangered','crimson']
#    clr_list = ['#F5DCA8','#F1CB7E','#ECBB53','#DE9E17','#AC7A12']
    clr_list = ['#74D7EE','#358791','#699B37','#E9AE2B','#C75252']
    dangye = ['1단계','1.5단계','2단계','2.5단계','4단계']
    dan = ['1단','1.5','2단','2.5','4']


    # 범례를 쓰기위한 구간
    #plt.plot(pdata_sum_x , pdata_sum['총신규확진자수'].to_list() , color='black' , 
    #                    linewidth=2.0 , label = 'corona')
    # 범례를 쓰기위한 구간
    for idx , i in enumerate(clr_list):
        plt.fill_between(pdata_sum_x[0:0] , pdata_sum_y[0:0], facecolor=i , alpha=1 , label=dangye[idx])
    # 구간별 색칠 막대그래프 생성  
    for i in range(0, len(temp_start)):
        for idx, j in enumerate(dan):
            if georidoogi_gov_summa[i].find(j) >= 0:
                plt.bar(pdata_sum_x[temp_start[i]:temp_end[i]] , 
                            pdata_sum_y[temp_start[i]:temp_end[i]],color = clr_list[idx] , alpha=1) 
    plt.legend(loc = 'upper left')  
    plt.title("서울 유동인구 , 신규확진자수 그래프 ",fontsize=15)
    #plt.show()
    #plt.cla()
    # 1, 1.5, 2, 2.5 4단계
    georidoogi_start =  ['2020-02-29' , '2020-03-22' , '2020-04-20' , '2020-05-06'  , '2020-08-16', '2020-08-30' , '2020-09-14' , '2020-09-28' ,  '2020-10-12' , '2020-11-19', '2020-12-08', '2021-02-15', '2021-07-12']
    georidoogi_end =    ['2020-03-21' , '2020-04-19' , '2020-05-05' , '2020-08-15' , '2020-08-29' , '2020-09-13', '2020-09-27' , '2020-10-11' ,  '2020-11-18' , '2020-12-07',  '2021-02-14', '2021-07-11', '2021-07-27'] # 8.8까지지만 자료가 7.27이 끝이므로
    georidoogi_gov_summa = ['2단계' ,    '2.5단계',       '2단계',        '1단계'       , '2단계'  ,     '2.5단계',    '2단계',       '2.5단계',       '1단계',       '1.5단계',    '2.5단계',    '2단계',    '4+단계']
    # datetime 변환 비교위함
    georidoogi_start = pd.to_datetime(georidoogi_start , format = '%Y-%m-%d')
    georidoogi_end = pd.to_datetime(georidoogi_end , format = '%Y-%m-%d')
    # 거리두기 정책기간 별로 인덱싱
    rate_start , rate_end , temp_dangye = geori_index(georidoogi_start , georidoogi_end , pdata_sum , georidoogi_gov_summa)
    temp_dangye = temp_dangye.dropna(axis=0)

    rate_x = []
    rate_y = []
    # 서울전체 유동인구(대중교통이용자)의 평균과 증감율 설정 
    for i in range(0, len(rate_start)):
        rate_y.append( round(temp_dangye.loc[rate_start[i]:rate_end[i]]['승하차총승객수'].mean() , 2))
        num = int((rate_start[i]+ rate_end[i]) / 2)
        rate_x.append( georidoogi_start[i] + (georidoogi_end[i]-georidoogi_start[i]) / 2)
    plt.plot(rate_x ,rate_y , color='#086A87', marker='o')
    
    real_rate = [ round( (rate_y[i]-rate_y[i-1])/rate_y[i-1]*100 ,2) for i in range(1,len(rate_y)) ]
    # 그래프에 증감율 텍스트로 표시
    for x, y in enumerate(real_rate):
        txt = "%d%%" %y
        plt.text(rate_x[x+1], rate_y[x+1], txt, fontsize=18, color='k' , weight="bold" , 
                        horizontalalignment='center', verticalalignment='bottom')

    plt.legend(loc = 'upper left')  
    plt.title("서울 유동인구,신규확진자수,거리두기 단계별 증감율" ,fontsize=15)

    plt.show()
    #----------------------

import json
import folium
from IPython.display import display
def gu_rate_map():
    colnames=['SIG_KOR_NM', '사용일자', '승하차총승객수'] 
    file_path = 'C:\\Users\\ksy\\downloads\\seoul_gu_data.csv'
    pdata = pd.read_csv(file_path , encoding='cp949' , index_col=False , names=colnames)
    pdata = pdata.groupby(['SIG_KOR_NM' , '사용일자'] , as_index = False)['승하차총승객수'].sum()
    pdata['사용일자'] = pd.to_datetime(pdata['사용일자'] , format = '%Y-%m-%d')
    #print(pdata)
    pdata_gu = [ pdata[pdata['SIG_KOR_NM'] == i] for i in pdata['SIG_KOR_NM'].unique() ]
    # for i in pdata_gu:
    #     print(i)

    georidoogi_start =  ['2020-02-29' , '2020-03-22' , '2020-04-20' , '2020-05-06'  , '2020-08-16', '2020-08-30' , '2020-09-14' , '2020-09-28' ,  '2020-10-12' , '2020-11-19', '2020-12-08', '2021-02-15', '2021-07-12']
    georidoogi_end =    ['2020-03-21' , '2020-04-19' , '2020-05-05' , '2020-08-15' , '2020-08-29' , '2020-09-13', '2020-09-27' , '2020-10-11' ,  '2020-11-18' , '2020-12-07',  '2021-02-14', '2021-07-11', '2021-07-27'] # 8.8까지지만 자료가 7.27이 끝이므로
    georidoogi_gov_summa = ['2단계' ,    '2.5단계',       '2단계',        '1단계'       , '2단계'  ,     '2.5단계',    '2단계',       '2.5단계',       '1단계',       '1.5단계',    '2.5단계',    '2단계',    '4+단계']
    georidoogi_start = pd.to_datetime(georidoogi_start , format = '%Y-%m-%d')
    georidoogi_end   = pd.to_datetime(georidoogi_end , format = '%Y-%m-%d')

    final_rate = []
    for j in pdata_gu:
        rate_start , rate_end , temp_dangye = geori_index(georidoogi_start , georidoogi_end , j.reset_index() , georidoogi_gov_summa)
        temp_dangye = temp_dangye.dropna(axis=0)
        # print(rate_start)
        # print(rate_end)
        # print(temp_dangye)

        #---------------------------------------------------------------------------------
        rate_x = [] # 거리두기 정책기간 중간 날짜
        rate_y = [] # 거리두기 정책기간 내에 승하차총승객수 평균

        for i in range(0, len(rate_start)):
            rate_y.append( round(temp_dangye.loc[rate_start[i]:rate_end[i]]['승하차총승객수'].mean() , 2))
            num = int((rate_start[i]+ rate_end[i]) / 2)
            rate_x.append( georidoogi_start[i] + (georidoogi_end[i]-georidoogi_start[i]) / 2)
        #print("-----------------------------------------------2")    
        # for idx , i in enumerate(rate_x):
        #     print(i , "  " ,  rate_y[idx])
        plt.plot(rate_x ,rate_y , color='#086A87', marker='o')
        
        #text 쓰는과정 사실상 없어도 되긴 함
        real_rate = [ round( (rate_y[i]-rate_y[i-1])/rate_y[i-1]*100 ,2) for i in range(1,len(rate_y)) ]
    #    print(real_rate)
        
        df = pd.DataFrame(data = {'사용일자':rate_x[1:] , '증감율':real_rate , '유동평균':rate_y[1:]} )
        gu = [j.iloc[0]['SIG_KOR_NM'] for _ in range(0,len(real_rate))]
        df = df.assign(SIG_KOR_NM = gu)
        final_rate.append(df)

        for x, y in enumerate(real_rate):
            txt = "%d%%" %y
            plt.text(rate_x[x+1], rate_y[x+1], txt, fontsize=18, color='k' , weight="bold" , 
                            horizontalalignment='center', verticalalignment='bottom')

        # 비율 구하려고 발악중--
    #print(len(final_rate) , len(pdata['SIG_KOR_NM'].unique()) )
    final_rate = pd.concat(final_rate, ignore_index=True)
    print(final_rate)
    final_rate_4 = final_rate[final_rate['사용일자'] == '2021-07-19 12:00:00'] #4단계 넘어갈때 증감율
    print(final_rate_4)
    plt.legend(loc = 'upper left')  
    plt.title("자치구 , 거리두기정책별 유동인구 증감율 ",fontsize=15)

    plt.cla()
    ax = sns.lineplot(x='사용일자', 
                  y='유동평균', 
                  hue='SIG_KOR_NM',
                  data=final_rate)
    plt.title('자치구 , 거리두기정책별 유동인구평균', fontsize=20)
    plt.ylabel('증감율', fontsize=14)
    plt.xlabel('Date', fontsize=14)
    plt.legend(fontsize=12, loc='best')
    plt.show()

    geo_path = 'C:\\Users\\ksy\\downloads\\skorea_municipalities_geo_simple.json'
    geo_str = json.load(open(geo_path, encoding='utf-8'))
    #print(json.dumps(geo_str, indent="\t") )
    seoul_map = folium.Map(location=[37.5502, 126.982], zoom_start=10.5, titles='cartodbpositron')
    seoul_map.choropleth(geo_data=geo_str,
                        data=final_rate_4,
                        columns=['SIG_KOR_NM', '증감율'],
                        fill_color='OrRd',      #RdPu, OrRd, YlOrRd
                        key_on='feature.properties.name',
                        highlight=True,
                        fill_opacity=0.5, line_opacity=1,
                        legend_name='population(people)')

    seoul_map.save('seoul_map.html')
    seoul_map
        #---------------------------------------------------------------------------------
    # 위에 부터 거리두기를 잘 지킨 순서
    print(final_rate_4.sort_values(by = ['증감율'])  )
gu_corona()
#gu_rate_map()

def temp():
    file_path = 'C:\\Users\\ksy\\downloads\\total_corona.csv'
    pdata = pd.read_csv(file_path , encoding='cp949' , index_col=False )
    pdata = pdata[['기준일' , '신규사망자']]
    pdata['기준일'] = pd.to_datetime(pdata['기준일'] , format = '%Y%m%d' )
    print(pdata)
    plt.plot(pdata['기준일'].to_list() , pdata['신규사망자'].to_list() , color='black' , 
                        linewidth=2.0 , label = '신규사망자수')
    plt.show()

#temp()

# %%

