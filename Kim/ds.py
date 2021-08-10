#%%
# -*- coding: utf-8 -*-
from re import L
import pandas as pd
from statistics import mean
import matplotlib.pyplot as plt # 막대그래프
#import seaborn as sns  # 

from matplotlib import rcParams
import matplotlib
from matplotlib import font_manager, rc
from pandas.io.parsers import count_empty_vals
matplotlib.font_manager._rebuild()
import matplotlib.dates as mdates

#한글깨짐 폰트설정
font_path = 'C:\\Users\\ksy\\Downloads\\MaruBuri-Regular\\MaruBuri-Regular.ttf'
font = font_manager.FontProperties(fname=font_path, size=18).get_name()
rc('font' , family = font)
plt.rcParams['axes.unicode_minus'] = False #한글 폰트 사용시 마이너스 폰트 깨짐 해결


def corona(): # 파일 읽어오기
#    file_path = 'C:\\Users\\ksy\\downloads\\CARD_SUBWAY_MONTH_202106.csv'
    file_path = 'C:\\Users\\ksy\\downloads\\total_corona_count.csv'
    pdata = pd.read_csv(file_path , sep =',', encoding='euc-kr')
#    pdata = pd.read_csv(file_path2 , sep ='\t')

    print(pdata.columns)
    corona_col = [i for i in pdata.columns]
    # index 타입으로 되어있는 컬럼들을 리스트로 변환

    #.sort_values()를 사용하여 데이터 정렬
    # 자료의 기준일이 역순이므로  
    pdata_sort = pdata.sort_values(by= "기준일" , ascending=True)
    print(pdata_sort.head())
    
    #선그래프
    plt.plot(pdata_sort["기준일"] , pdata_sort["일일 확진자 수"])
    plt.show()

    # 한 그래프에 선 두개 표현
    plt.plot(pdata_sort["기준일"], pdata_sort["일일 확진자 수"])
    plt.plot(pdata_sort["기준일"], pdata_sort["일일 검사 수"])
    # 화면에 그래프를 보여줍니다
    plt.show()

    #Axis and Labels
    #종종 그래프의 특정 영역을 확대하거나 강조하고 싶을 수 있습니다. 
    # 이 때 보여줄 축의 범위를 .axis() 함수로 지정할 수 있습니다. 
    # .axis() 함수는 [ x_min, x_max, y_min, y_max ] 를 파라미터로 전달
    plt.plot(pdata_sort["기준일"], pdata_sort["일일 확진자 수"])
    plt.axis([20200201, 20201201, 0 , 10000] )
    plt.show()

    # 전일대비 칸을 추가?
    # 막대 그래프
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    ax.bar(x=pdata_sort["기준일"].astype(str), height=pdata_sort["일일 확진자 수"])
    plt.show()

def subway():
    file_path = 'C:\\Users\\ksy\\downloads\\CARD_SUBWAY_MONTH_202105.csv'
#    pdata = pd.read_csv(file_path , sep =',', encoding='euc-kr')
    #index_col = False 꼭필요하다 꼭
    pdata = pd.read_csv(file_path , sep =',' , index_col=False)
#    pdata = pd.read_csv(file_path , encoding='CP949')
#    seoul_station = ["가락시장","가산디지털단지","가양","가오리",	"가좌",	"강남",	"강남구청",	"강동",	"강동구청",	"강변",	"강일",	"개롱",	"개봉",	"개포동",	"개화",	"개화산",	"거여",	"건대입구",	"경복궁",	"경찰병원",	"고덕",	"고려대",	"고속터미널",	"공덕",	"공릉",	"공항시장",	"광나루",	"광운대",	"광화문",	"광흥창",	"교대",	"구로",	"구로디지털단지",	"구룡",	"구반포",	"구산",	"구의",	"구일",	"구파발",	"국회의사당",	"군자",	"굽은다리",	"금천구청",	"금호",	"길동",	"길음",	"김포공항",	"까치산",	"낙성대",	"남구로",	"남부터미널",	"남성",	"남영",	"남태령",	"내방",	"노들",	"노량진",	"노원",	"녹번",	"녹사평",	"녹천",	"논현",	"답십리",	"당고개",	"당산",	"대림",	"대모산입구",	"대방",	"대청",	"대치",	"대흥",	"도곡",	"도림천",	"도봉",	"도봉산",	"독립문",	"독바위",	"독산",	"돌곶이",	"동대문",	"동대문역사문화공원",	"동대입구",	"동묘앞",	"동작",	"둔촌동",	"둔촌오륜",	"등촌",	"디지털미디어시티",	"뚝섬",	"뚝섬유원지",	"마곡",	"마곡나루",	"마들",	"마장",	"마천",	"마포",	"마포구청",	"망우",	"망원",	"매봉",	"먹골",	"면목",	"명동",	"명일",	"목동",	"몽촌토성",	"무악재",	"문래",	"문정",	"미아",	"미아사거리",	"반포",	"발산",	"방배",	"방이",	"방학",	"방화",	"버티고개",	"보라매",	"보문",	"복정",	"봉은사",	"봉천",	"봉화산",	"북한산보국문",	"북한산우이",	"불광",	"사가정",	"사당",	"사평",	"삼각지",	"삼성",	"삼성중앙",	"삼양",	"삼양사거리",	"삼전",	"상계",	"상도",	"상봉",	"상수",	"상왕십리",	"상월곡",	"상일동",	"새절",	"샛강",	"서강대",	"서대문",	"서빙고",	"서울대입구",	"서울숲",	"서울역",	"서초",	"석계",	"석촌",	"석촌고분",	"선릉",	"선유도",	"선정릉",	"성수",	"성신여대입구",	"솔샘",	"솔밭공원",	"송정",	"송파",	"송파나루",	"수락산",	"수색",	"수서",	"수유",	"숙대입구",	"숭실대입구",	"시청",	"신금호",	"신길",	"신내",	"신논현",	"신답",	"신당",	"신대방",	"신대방삼거리",	"신도림",	"신림",	"신목동",	"신반포",	"신방화",	"신사",	"신설동",	"신용산",	"신이문",	"신정",	"신정네거리",	"신촌(2)",	"신촌(경)",	"신풍",	"쌍문",	"아차산",	"아현",	"안국",	"안암",	"암사",	"압구정",	"압구정로데오",	"애오개",	"약수",	"양원",	"양재",	"양재시민의숲",	"양천구청",	"양천향교",	"양평(5)",	"어린이대공원",	"언주",	"여의나루",	"여의도",	"역삼",	"역촌",	"연신내",	"염창",	"영등포",	"영등포구청",	"영등포시장",	"오금",	"오류동",	"오목교",	"옥수",	"온수",	"올림픽공원",	"왕십리",	"외대앞",	"용답",	"용두",	"용마산",	"용산",	"우장산",	"월계",	"월곡",	"월드컵경기장",	"을지로입구",	"을지로3가",	"을지로4가",	"응봉",	"응암",	"이대",	"이수",	"이촌",	"이태원",	"일원",	"잠실",	"잠실나루",	"잠실새내",	"잠원",	"장승배기",	"장지",	"장한평",	"정릉",	"제기동",	"종각",	"종로3가",	"종로5가",	"종합운동장",	"중계",	"중곡",	"중랑",	"중앙보훈병원",	"중화",	"증미",	"증산",	"창동",	"창신",	"천왕",	"천호",	"청구",	"청담",	"청량리",	"충무로",	"충정로",	"태릉입구",	"하계",	"학동",	"학여울",	"한강진",	"한남",	"한성대입구",	"한성백제",	"한양대",	"한티",	"합정",	"행당",	"혜화",	"홍대입구",	"홍제",	"화계",	"화곡",	"화랑대",	"회기",	"회현",	"효창공원앞",	"흑석"	]
    print("행과 열의 개수는 " , pdata.shape)
    # 어떤 컬럼들이 있는지 
    print(pdata.columns)
    # 각 컬럼들의 데이터 타입을 알려준다.
    print(pdata.dtypes)

    print(pdata.head())
    # 생략가능 pdata.columns[] 이런식으로 쓰면 되지 않을까 싶음
    # index 타입으로 되어있는 컬럼들을 리스트로 변환
    subway_col = [i for i in pdata.columns]
    #종합 통계를 불러오는 함수
    print(pdata.describe())

#    print(pdata["사용일자"])
#    print(pdata["노선명"]

    print(pdata.groupby(['사용일자'])["하차총승객수"].sum())
    #시각화 사용일자 넣으면 키에러 

    #
    pdata["승하차총승객수"] = pdata["승차총승객수"] + pdata["하차총승객수"]
    print(pdata.head())

    # 사용일자 별로 묶어서 승하차총승객수만 나오는 테이블 저장
    pdata_sum = pdata.groupby(['사용일자'], as_index = False)["승하차총승객수"].sum()
#    pdata_sum = pdata.groupby(['사용일자'])["승하차총승객수"].sum()
    print( "pdata_sum groupby 사용일자 승하차총승객수" )
    print( pdata_sum.head() )
    print( pdata_sum.dtypes )

    #pdata_sum["사용일자"] = pd.to_datetime(pdata_sum["사용일자"] #1970-01-01 00:00:00.020210501
    pdata_sum["사용일자"] = pd.to_datetime(pdata_sum["사용일자"], format='%Y%m%d')
#    subDay['사용일자'] = pd.to_datetime(subDay['사용일자'].astype('str'), errors = 'coerce')
    print(pdata_sum.dtypes)

    print( pdata_sum.head() )

#----------------------------선그래프?----------------------
    plt.plot(pdata_sum["사용일자"] , pdata_sum["승하차총승객수"])
    plt.show()
#----------------------------막대그래프----------------------
    plt.bar(pdata_sum["사용일자"] , pdata_sum["승하차총승객수"])
    plt.show()

#----------------------------스타일 추가----------------------
    # 파선(Dashed)
    #plt.plot(pdata_sum["사용일자"], pdata_sum["승하차총승객수"], linestyle='--')
    # 점선(Dotted)
    plt.plot(pdata_sum["사용일자"], pdata_sum["승하차총승객수"], linestyle=':')
    # 실선(No line)
#    plt.plot(pdata_sum["사용일자"], pdata_sum["승하차총승객수"], linestyle='')
    plt.show()

    # 원(A circle)
    plt.plot(pdata_sum["사용일자"], pdata_sum["승하차총승객수"], marker='o')
    # 정사각형(A square)
#    plt.plot(pdata_sum["사용일자"], pdata_sum["승하차총승객수"], marker='s')
    # 별(A star)
#    plt.plot(pdata_sum["사용일자"], pdata_sum["승하차총승객수"], marker='*')
    plt.show()

#     a_mean = pdata["승차총승객수"].mean()
#     a_mean = pdata[subway_col[3]].mean()
#     print(a_mean)

#     b_mean = pdata[ pdata["노선명"] == '3호선' ]["승차총승객수"].sum()
#     print("승차합" , b_mean)
    
#     b_mean = pdata[ (pdata["사용일자"] == 20210601) & (pdata["역명"] == "어린이대공원(세종대)") ]["승차총승객수"].sum()
#     print(b_mean)

#     sun = pdata["노선명"].unique()
# #    print(sun)

#     station = pdata["역명"].unique()
#     print(len(station))
    # for i in station:
    #     print(i)
#    print(pdata["역명"].unique())


#    print(seoul_station)

    # print(len(station) , len(seoul_station) )
    # cnt =0
    # for i in station:
    #     if i in seoul_station:
    #         cnt +=1
    # print(cnt)

def subway_st(all_data):
    # file_path = 'C:\\Users\\ksy\\downloads\\CARD_SUBWAY_MONTH_202105.csv'
    # pdata = pd.read_csv(file_path , sep =',' , index_col=False)

    #넘겨받은 all_data 를 pdata로 바꾸고 역명체크단계
    pdata = all_data
    seoul_station = ["가락시장","가산디지털단지","가양","가오리",	"가좌",	"강남",	"강남구청",	"강동",	"강동구청",	"강변",	"강일",	"개롱",	"개봉",	"개포동",	"개화",	"개화산",	"거여",	"건대입구",	"경복궁",	"경찰병원",	"고덕",	"고려대",	"고속터미널",	"공덕",	"공릉",	"공항시장",	"광나루",	"광운대",	"광화문",	"광흥창",	"교대",	"구로",	"구로디지털단지",	"구룡",	"구반포",	"구산",	"구의",	"구일",	"구파발",	"국회의사당",	"군자",	"굽은다리",	"금천구청",	"금호",	"길동",	"길음",	"김포공항",	"까치산",	"낙성대",	"남구로",	"남부터미널",	"남성",	"남영",	"남태령",	"내방",	"노들",	"노량진",	"노원",	"녹번",	"녹사평",	"녹천",	"논현",	"답십리",	"당고개",	"당산",	"대림",	"대모산입구",	"대방",	"대청",	"대치",	"대흥",	"도곡",	"도림천",	"도봉",	"도봉산",	"독립문",	"독바위",	"독산",	"돌곶이",	"동대문",	"동대문역사문화공원",	"동대입구",	"동묘앞",	"동작",	"둔촌동",	"둔촌오륜",	"등촌",	"디지털미디어시티",	"뚝섬",	"뚝섬유원지",	"마곡",	"마곡나루",	"마들",	"마장",	"마천",	"마포",	"마포구청",	"망우",	"망원",	"매봉",	"먹골",	"면목",	"명동",	"명일",	"목동",	"몽촌토성",	"무악재",	"문래",	"문정",	"미아",	"미아사거리",	"반포",	"발산",	"방배",	"방이",	"방학",	"방화",	"버티고개",	"보라매",	"보문",	"복정",	"봉은사",	"봉천",	"봉화산",	"북한산보국문",	"북한산우이",	"불광",	"사가정",	"사당",	"사평",	"삼각지",	"삼성",	"삼성중앙",	"삼양",	"삼양사거리",	"삼전",	"상계",	"상도",	"상봉",	"상수",	"상왕십리",	"상월곡",	"상일동",	"새절",	"샛강",	"서강대",	"서대문",	"서빙고",	"서울대입구",	"서울숲",	"서울역",	"서초",	"석계",	"석촌",	"석촌고분",	"선릉",	"선유도",	"선정릉",	"성수",	"성신여대입구",	"솔샘",	"솔밭공원",	"송정",	"송파",	"송파나루",	"수락산",	"수색",	"수서",	"수유",	"숙대입구",	"숭실대입구",	"시청",	"신금호",	"신길",	"신내",	"신논현",	"신답",	"신당",	"신대방",	"신대방삼거리",	"신도림",	"신림",	"신목동",	"신반포",	"신방화",	"신사",	"신설동",	"신용산",	"신이문",	"신정",	"신정네거리",	"신촌(2)",	"신촌(경)",	"신풍",	"쌍문",	"아차산",	"아현",	"안국",	"안암",	"암사",	"압구정",	"압구정로데오",	"애오개",	"약수",	"양원",	"양재",	"양재시민의숲",	"양천구청",	"양천향교",	"양평(5)",	"어린이대공원",	"언주",	"여의나루",	"여의도",	"역삼",	"역촌",	"연신내",	"염창",	"영등포",	"영등포구청",	"영등포시장",	"오금",	"오류동",	"오목교",	"옥수",	"온수",	"올림픽공원",	"왕십리",	"외대앞",	"용답",	"용두",	"용마산",	"용산",	"우장산",	"월계",	"월곡",	"월드컵경기장",	"을지로입구",	"을지로3가",	"을지로4가",	"응봉",	"응암",	"이대",	"이수",	"이촌",	"이태원",	"일원",	"잠실",	"잠실나루",	"잠실새내",	"잠원",	"장승배기",	"장지",	"장한평",	"정릉",	"제기동",	"종각",	"종로3가",	"종로5가",	"종합운동장",	"중계",	"중곡",	"중랑",	"중앙보훈병원",	"중화",	"증미",	"증산",	"창동",	"창신",	"천왕",	"천호",	"청구",	"청담",	"청량리",	"충무로",	"충정로",	"태릉입구",	"하계",	"학동",	"학여울",	"한강진",	"한남",	"한성대입구",	"한성백제",	"한양대",	"한티",	"합정",	"행당",	"혜화",	"홍대입구",	"홍제",	"화계",	"화곡",	"화랑대",	"회기",	"회현",	"효창공원앞",	"흑석"	]
    
    #엑셀의 전체 역들 중복제거
    station = pdata["역명"].unique()
    print(len(station) , len(seoul_station) )

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

    print( all_data[all_data["역명"] == '신촌'])
    print( all_data[all_data["역명"] == '양평'])

    print("station , seoul_station , same_st  " , len(station) , len(seoul_station) , len(same_st))
    print("---------------------------------------------------------------------")
    print("분류되기 전에 역명의 길이"  ,  len(all_data["역명"].unique()))
    seoul_data = all_data[ all_data["역명"].isin(same_st) ]
    print("---------------------------------------------------------------------")
    print("분류된 역명의 길이 " , len(seoul_data["역명"].unique()))
    print("---------------------------------------------------------------------")
    print(seoul_data) # 위의 신촌 2개 양평 1개가 빠진 데이터 채워넣으면 된다.
    return seoul_data



from glob import glob # 파일 경로를 조작할 수 있다.
import chardet
def subway_all_file():
    # 해당 디렉토리 내에 .csv 파일을 다 불러와서 리스트에 담아준다.
    file_path = glob('C:\\Users\\ksy\\downloads\\data\\*.csv')
    all_file = []
    print(file_path)
    #인코딩 확인 코드-----------------------------------------------
    for path in file_path:
        rawdata = open(path, 'rb').read() #파일 열고
        result = chardet.detect(rawdata) # 인코딩 형식 검사하고
        charenc = result['encoding']  # 인코딩 결과 확인하고
        #print(charenc)    
    #인코딩 확인 코드 마무리 ----------------------------------------
        # utf8 error -> engine='python' 으로 해결 (무시하는듯 한글깨짐) 
        # 위에서 확인한 인코딩을 넣어서 append
        #위에 인코딩 확인코드 시간 줄일 필요 있을 듯 
        csvfile = pd.read_csv(path ,encoding = charenc , index_col=False)
        all_file.append(csvfile)
        #print(csvfile.head())
    
    # 위에서 모든 엑셀 파일을 열어서 내용을 담은 all_file을 같은 컬럼이니 합친다.
    all_data = pd.concat(all_file, ignore_index=True)
    all_data["사용일자"] = pd.to_datetime(all_data["사용일자"], format='%Y%m%d')
    #print("전체 엑셀 데이터가 합쳐진 첫번째")
    #print(all_data)

    # 이제 모아놓은 전 엑셀 데이터를 서울을 주소지로 갖는 역으로 필터링 해주어야 한다.
    all_data = subway_st(all_data)
    print("역명이 분류된 두번째 전체 데이터")
    print(all_data) 

#--시각화 진행 함수로 만들기도 가능----------------------------------------------------------------------------------
    subway_col = [i for i in all_data.columns]

    # 새로운 컬럼 생성 (승하차총승객수)
    all_data["승하차총승객수"] = all_data["승차총승객수"] + all_data["하차총승객수"]

    # 사용일자 별로 묶어서 승하차총승객수만 나오는 테이블 저장
    pdata_sum = all_data.groupby(['사용일자'], as_index = False)["승하차총승객수"].sum()
    print( "pdata_sum groupby 사용일자 승하차총승객수" )
    print(pdata_sum)

#----------------------------선그래프?----------------------
    #plt.plot(pdata_sum["사용일자"] , pdata_sum["승하차총승객수"])
    #plt.show()
#----------------------------막대그래프----------------------
    #plt.bar(pdata_sum["사용일자"] , pdata_sum["승하차총승객수"])
    #plt.show()
    
    print('-----------------------------------------------------------')
    return all_data #잠깐 all_data 사용중 원래 pdata_sum 리턴


from matplotlib import colors as mcolors
#import datetime
def gu_corona():
    
    file_path = 'C:\\Users\\ksy\\downloads\\서울특별시 코로나19 자치구별 확진자 발생동향.csv'
    pdata = pd.read_csv(file_path , encoding ='cp949' , index_col=False)

    #뒤에 분초를 떼어버렸다.
    pdata["자치구 기준일"] = pdata["자치구 기준일"].str.slice(start=0 , stop=10)
    print(pdata["자치구 기준일"])
    print(pdata.dtypes)
    # 날짜 변환
    pdata["자치구 기준일"] = pd.to_datetime(pdata["자치구 기준일"] , format = '%Y.%m.%d')
    # 날짜기준 정렬
    pdata = pdata.sort_values(by = ['자치구 기준일'])  
#--------------------------------------------------------------------
    # pd.set_option('mode.chained_assignment',  None) # ↓자꾸 에러떠서 경고문 끔
    
    # 자치구별 신규확진자수 추출해 데이터프레임생성 -------------------
    new = pdata.filter(regex='기준일|추가') # 아래랑 주석 바꾸려면 밑에 수치부분도 주석풀기
    #new = pdata.filter(regex='기준일|전체')
    new['총신규확진자수'] = new.iloc[:,1:26].sum(axis=1)
    new = new[['자치구 기준일' , '총신규확진자수']]
    print('???????????????????????????????????????????????????????')
    print(new.head())

#--------------------------------------------------------------------

    # 행열전환 자치구가 행으로 확진자수가  자세한 설명 아래 링크 참조
    # https://computer-science-student.tistory.com/158
    pdata = pdata.transpose()
    pdata.rename(columns = pdata.iloc[0] , inplace=True)
    pdata = pdata.drop(pdata.index[0])
    # print(pdata)
    # #------------------------------------------------------------
    # print()
    # print(pdata[1::2]) #추가 부분
    # print(pdata[0::2]) #전체 부분만

    # 종로 - 기타
    pdata_add = pdata[1::2]
    pdata_all = pdata[0:-1:2]

    # print(pdata_all.columns)
    # print(type(pdata_all.columns))
    # print(pdata_add.columns[0])
    # print(len(pdata_all.index))
    # print(len(pdata_add[pdata_add.columns[0]]))

    #파이차트
    #plt.pie(pdata_add[pdata_add.columns[-1]], labels=pdata_all.index, autopct='%.1f%%')
    #plt.title(str(pdata_add.columns[-1]) , fontsize = 15)
    #plt.show()

    #종로구 전체에대해서 확진자수 그래프 index[0]에서 0을 i로주고 반복문 돌리면 전체 자치구
    # print( pdata_all.loc[pdata_all.index[0]] )
    # columns 는 날짜  /  index[0] - 자치구들
    # plt.plot(pdata_all.columns , pdata_all.loc[pdata_all.index[0]])
    # plt.title(pdata_all.index[0],fontsize=15)
    # plt.show()

#--------------------------------------------------------------------------------------
    #거리두기 단계별 시작과 끝 담기
    # df = pdata_all.sort_values(by = ['확진자수'], ascending = False)       
                        #  거리두기    강화된거리두기     일부 조치완화    생활거리두기    3단계거리두기   3단계거리두기   4단계거리두기  4단계거리두기  4단계거리두기   4단계거리두기       5단계         5단계         특별대책      특별대책            
    georidoogi_start =  ['2020-02-29' , '2020-03-22' , '2020-04-20' , '2020-05-06' , '2020-06-28' , '2020-08-16', '2020-08-30' , '2020-09-14' , '2020-09-28' ,  '2020-10-12' , '2020-11-19', '2020-12-08', '2020-12-23', '2021-01-16', '2021-02-06', '2021-02-15', '2021-07-12']
    georidoogi_end =    ['2020-03-21' , '2020-04-19' , '2020-05-05' , '2020-06-27' , '2020-08-15' , '2020-08-29' , '2020-09-13', '2021-09-27' , '2020-10-11' ,  '2020-11-18' , '2020-12-07', '2020-12-22', '2021-01-15', '2021-02-05', '2021-02-14', '2021-07-11', '2021-07-27'] # 8.8까지지만 자료가 7.27이 끝이므로
    georidoogi_gov = [ '거리두기'  , '강화된거리두기' ,'일부 조치완화','생활거리두기', '3단계거리두기' , '3단계거리두기','4단계거리두기','4단계거리두기', '4단계거리두기','4단계거리두기','5단계거리두기','5단계거리두기','특별대책'   ,'특별대책' ,   '특별대책',   '추가조치',   '추가조치']
    georidoogi_gov_summa = ['2단계' ,    '2.5단계',       '2단계',        '1단계',      '1단계'       , '2단계'  ,     '2.5단계',    '2단계',       '2.5단계',       '1+단계',       '1.5단계',    '2.5단계',    '2.5+단계',    '2.5-단계',  '2.5--단계',    '2단계',    '4+단계']
    print( len(georidoogi_start) , len(georidoogi_end) , len(georidoogi_gov_summa))
    
    all_data = subway_all_file()
    pdata_sum = all_data.groupby(['사용일자'], as_index = False)["승하차총승객수"].sum()

    new.rename(columns = {'자치구 기준일' : '사용일자'}, inplace = True)
    pdata_sum = pd.merge( new ,pdata_sum, how='left', on='사용일자' )
    pdata_sum['총신규확진자수'] = pdata_sum['총신규확진자수'].values * 12000  # 추가확진자(신규확진자)
    # pdata_sum['총신규확진자수'] = pdata_sum['총신규확진자수'].values * 180 # 누적확진자수그래프           
    print(pdata_sum)

    # 비교위해 리스트 datetime 으로 변환 
    georidoogi_start = pd.to_datetime(georidoogi_start , format = '%Y.%m.%d')
    georidoogi_end = pd.to_datetime(georidoogi_end , format = '%Y.%m.%d')
    # pdata_sum 내부에 날짜의 index를 담기위함
    temp_start = []
    temp_end = []
    for idx , i in enumerate(pdata_sum['사용일자']):
        for j in georidoogi_start:
            if i == j:
                temp_start.append(idx)
        for k in georidoogi_end:
            if i ==k:
                temp_end.append(idx)
            if i.year == 2021 and i.month == 7 and i.day == 27:
                if idx not in temp_end:
                    temp_end.append(idx)

    print("거리두기 정책 시작일 " ,len(temp_start) ,  temp_start) #실제 index 가 담겨있다.
    print("거리두기 정책 종료일 " ,len(temp_end) , temp_end)
    print(pdata_sum['사용일자'][516])

    # 색상 리스트 불러오는 구간---------------------------------------------------------
    colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
    # Sort colors by hue, saturation, value and name.
    by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                    for name, color in colors.items())
    sorted_names = [name for hsv, name in by_hsv]
    print("색상 개수 " , len(sorted_names))
    #--------------------------------------------------------------------------------------
    # pdata_all_x = [date.to_pydatetime() for date in pdata.columns ]
    pdata_all_x = pdata.columns.to_list()
    pdata_all_y = pdata_all.loc[pdata_all.index[0]].to_list()

    pdata_sum_x = pdata_sum['사용일자'].to_list()
    pdata_sum_y = pdata_sum['승하차총승객수'].to_list()
    print("pdata_sum_x 의 개수는 " , len(pdata_sum_x))

    clr_list = ['aqua','deepskyblue','peru','orangered','crimson']
    dangye = ['1단계','1.5단계','2단계','2.5단계','4단계']
    dan = ['1단','1.5','2단','2.5','4']
    
    plt.plot(pdata_sum_x , pdata_sum['총신규확진자수'].to_list() , color='black' , linewidth=2.0 , label = 'corona')
    # 범례를 쓰기위한 구간
    for idx , i in enumerate(clr_list):
        plt.fill_between(pdata_sum_x[0:0] , pdata_sum_y[0:0], facecolor=i , alpha=1 , label=dangye[idx])
           
    # 구간별 색칠 막대그래프 생성  
    for i in range(0, len(temp_start)):
        for idx, j in enumerate(dan):
            if georidoogi_gov_summa[i].find(j) >= 0:
                plt.bar(pdata_sum_x[temp_start[i]:temp_end[i]] , pdata_sum_y[temp_start[i]:temp_end[i]],color = clr_list[idx] , alpha=1) 
    plt.legend(loc = 'upper left')  
    plt.title("서울 유동인구 , 신규확진자수 그래프 ",fontsize=15)
    plt.show()

def gu_gu():
    file_path = 'C:\\Users\\ksy\\downloads\\서울역.csv'
    pdata = pd.read_csv(file_path , encoding ='cp949' , index_col=False)
    print(pdata.columns)
    print(pdata[pdata.columns[1]])

    # 위에 함수들에서 추출가능
    gu_lst = ['종로구','중구','용산구','성동구','광진구','동대문구','중랑구','성북구',
'강북구','도봉구','노원구','은평구','서대문구','마포구','양천구','강서구',
'구로구','금천구','영등포구','동작구','관악구','서초구','강남구','송파구','강동구']
    same_gu = []
    for i in range(len(gu_lst)):
        same_gu.append([])
        for j in range(len(pdata[pdata.columns[1]])): # 여기서 단어를 비교
            #print(pdata[pdata.columns[1]][j].find(gu_lst[i]) )
            if pdata[pdata.columns[1]][j].find(gu_lst[i]) >= 0 and gu_lst[i] not in same_gu[i]:
                same_gu[i].append(pdata[pdata.columns[0]][j])

    for i in range(len(same_gu)):
        for j in same_gu[i]:
            print(gu_lst[i] , j)

import seaborn as sns
import os 
import folium
from folium import plugins 
print(folium.__version__)
#googlemap
import googlemaps
def gu_subway():
    file_path = 'C:\\Users\\ksy\\downloads\\seoul_gu.csv'
    pdata = pd.read_csv(file_path , encoding ='utf-8' , index_col=False)
    #print(pdata)
    # 20년2월부터 21년7월까지 전체 데이터
    all_data = subway_all_file()
    #print(all_data)
    # 새로운 컬럼 생성 승하차총승객수
    all_data['승하차총승객수'] = all_data["승차총승객수"] + all_data["하차총승객수"]
    #print(all_data)

    #all_data["자치구"] = all_data[ all_data["역명"] == pdata['역명']
    add_gu_data = pd.merge(all_data , pdata, how='left', on='역명' )
    #print(add_gu_data)
    #print(add_gu_data.info()) #left 조인을 안하면 자치구가 3개 더 들어온다.
    #print(add_gu_data['자치구'].unique())
    # \xa0 없애는 코드
    add_gu_data['자치구'] = add_gu_data['자치구'].str.split().str.join(' ')
    #print(add_gu_data['자치구'].unique())

    #print(add_gu_data['승하차총승객수'])
    add_gu_data = add_gu_data[ ['사용일자','승하차총승객수','자치구'] ]
    print(add_gu_data[['사용일자','승하차총승객수','자치구']])
    #['사용일자'] = add_gu_data['사용일자'].values.astype(float)
 
    # 그룹별 집계하는 방법 - 일자별 집계
    add_gu_data = add_gu_data.groupby(['자치구','사용일자'], as_index = False)['승하차총승객수'].sum()
    print(add_gu_data.head())
    #add_gu_data.to_csv('C:\\Users\\ksy\\downloads\\seoul_gu_group.csv' , header=False , index=False)

    add_gu_data_top = add_gu_data.groupby(['자치구'], as_index = False)['승하차총승객수'].sum()
    add_gu_data_top = add_gu_data_top.sort_values(by= "승하차총승객수" , ascending=True)
    print(add_gu_data_top["자치구"])
    #add_gu_data.to_csv('C:\\Users\\ksy\\downloads\\seoul_gu_data.csv' , header=False , index=False)
    # 시각화 부분-------------------------------------------------------------------------------------------------------
    # lineplot 써서 모든 그래프 출력 자치구별로 색깔 자동변함
    ax = sns.lineplot(x='사용일자', 
                    y='승하차총승객수',
                    hue='자치구',
                     data=add_gu_data)
    plt.show()

from IPython.display import display
import geopandas as gpd
import fiona
from folium import Choropleth, Circle, Marker
def last_subway_corona():
    colnames=['SIG_KOR_NM', '사용일자', '승하차총승객수'] 
    file_path = 'C:\\Users\\ksy\\downloads\\seoul_gu_data.csv'
    pdata = pd.read_csv(file_path , encoding='cp949' , index_col=False , names=colnames)
    pdata = pdata.groupby(['SIG_KOR_NM'] , as_index = False)['승하차총승객수'].sum()
    print(pdata)

    #37.496555, 127.064000 , 강남구
    # 37.550230, 127.146991 , 강동구
    # 37.642472, 127.012612 , 강북구
    # 37.561297, 126.821522 , 강서구

    #seoul_file = "C:\\Users\\ksy\\Downloads\\CTPRVN_202101\\TL_SCCO_CTPRVN.shp"
    seoul_file = "C:\\Users\\ksy\\Downloads\\SIG_202101\\TL_SCCO_SIG.shp"
    seoul = gpd.read_file(seoul_file , encoding = 'cp949')
    seoul = seoul.drop("SIG_ENG_NM",axis=1)
    pd.set_option('display.max_columns', None)
    print(seoul[seoul['SIG_KOR_NM'].isin(pdata['SIG_KOR_NM'])] )
    seoul = seoul[seoul['SIG_KOR_NM'].isin(pdata['SIG_KOR_NM'])]
    seoul = seoul[seoul['SIG_CD'].str.slice(start=0 , stop=2) == "11" ]

    #print(seoul)
    #seoul.plot(color='black')
    #좌표계 변경
    print("--------------------------------------------")
    print(seoul.crs)
    seoul_crs = seoul.to_crs(epsg=4326)
    print("과연 무엇이 나올까")
    print(seoul_crs.crs)
    print(seoul_crs.head())
    seoul = pd.merge( seoul ,pdata, how='left', on='SIG_KOR_NM' )
    print(seoul)
    # seoul = seoul.to_crs(epsg='4326')
    # seoul.plot(color='black')
    # ax = seoul.plot(column="SIG_KOR_NM", figsize=(10,8), alpha=0.8)
    # seoul.plot(ax = ax , column = '승하차총승객수', legend=True)
    # #pdata.plot(ax=ax, marker='v', color='black', label='Firestation')
    # ax.set_title("Seoul", fontsize=20)
    # ax.set_axis_off()
    # ax.legend(ax.lines, seoul['SIG_KOR_NM'] , loc='center left')
    # plt.show()

    seoul.geometry = seoul.buffer(0.001)
    seoul = seoul.dissolve(by='SIG_CD')
    ax = seoul.plot(figsize=(10, 8), column="SIG_KOR_NM", categorical=True,
                    cmap="tab20b", edgecolor="k", legend=True, legend_kwds={'loc': 3})
    seoul.plot(ax = ax, marker ='o'  , column = '승하차총승객수', legend=True)
    ax.set_title("구 별로 묶은 서울의 기초 구역도")
    ax.set_axis_off()
    plt.show()
    #plt.cla()

    
    seoul_gu = folium.Map(location = (37.5502, 126.982),
                                 zoom_start = 10.5, tiles='cartodbpositron')
    for _, r in seoul_crs.iterrows():
        # Without simplifying the representation of each borough,
        # the map might not be displayed
        sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j,
                            style_function=lambda x: {'fillColor': 'orange'})
        folium.Popup(r['SIG_KOR_NM']).add_to(geo_j)
        geo_j.add_to(seoul_gu)
                    
    # Project to NAD83 projected crs
    seoul = seoul.to_crs(epsg=2263)
    # Access the centroid attribute of each polygon
    seoul['centroid'] = seoul.centroid
    # Project to WGS84 geographic crs

    # geometry (active) column  좌표계변환
    seoul = seoul.to_crs(epsg=4326)
    # Centroid column  아마 저 popup 마커를 위해 중간좌표를 가져오는 코드일듯
    seoul['centroid'] = seoul['centroid'].to_crs(epsg=4326)

    print(seoul.head())
    for _, r in seoul.iterrows():
        lat = r['centroid'].y
        lon = r['centroid'].x
        folium.Marker(location=[lat, lon],
                    popup='{}'.format(r['SIG_KOR_NM'])).add_to(seoul_gu)
        folium.CircleMarker(location=[lat, lon], radius=r['승하차총승객수']/10000000,color='#3186cc',
                        fill_color='#3186cc', popup='{}'.format(r['SIG_KOR_NM'])).add_to(seoul_gu)
    display(seoul_gu)

# map_osm = folium.Map(location=[37.566345, 126.977893], zoom_start=17)
# folium.Marker([37.566345, 126.977893], popup='서울특별시청', icon=folium.Icon(color='red',icon='info-sign')).add_to(map_osm)
# folium.CircleMarker([37.5658859, 126.9754788], radius=100,color='#3186cc',fill_color='#3186cc', popup='덕수궁').add_to(map_osm)
# map_osm.save('d:/temp/chicken_data/map6.html')
    # folium.Choropleth(geo_data = seoul,
    #             data = seoul['승하차총승객수'],
    #             columns = ['SIG_KOR_NM','승하차총승객수'],
    #             fill_color="OrRd",legend_name='자치구 승하차총승객수').add_to(seoul_gu) 
    # print("---------------33")
    # print(seoul_gu)
    # seoul_gu

    # converted_json = seoul.to_json()
    # map = folium.Map(location=[37.5502, 126.982], zoom_start=11, tiles='Stamen Toner')

    # folium.GeoJson(
    #     converted_json,
    # ).add_to(map)

    # map
    # 자치구 별로 4개씩 묶어서 출력
    # cnt = 0
    # tit = ""
    # for i in add_gu_data['자치구'].unique():
    #     tit =  tit + i + ","
    #     #print(tit)
    #     plt.ylim(0 , 1500000)
    #     plt.plot(add_gu_data[add_gu_data['자치구']==i]['사용일자'].to_list() , add_gu_data[add_gu_data['자치구']==i]['승하차총승객수'].to_list())
    #     if cnt %4 == 0:
    #         plt.title( tit ,fontsize=15)
    #         plt.show()   
    #         plt.cla()
    #         tit = ""
    #     elif cnt == len(add_gu_data['자치구'].unique())-1:
    #         plt.title( tit ,fontsize=15)
    #         plt.show()     
    #     cnt+=1
    # 시각화 부분-------------------------------------------------------------------------------------------------------

    # sns.scatterplot(x='사용일자', y='승하차총승객수', data=add_gu_data)
    # plt.show()

# 해야할 내용
# seoul_station 역명에 신촌 양평? 포함되지 않는거 해결
# 전체적으로 이어서 사용할 수 있게 다듬기
#corona()            # 전체 확진자 수
#subway()            # 서울 지하철 승하차 1개 파일로 조작 익숙해지기
#subway_st()         # 서울에 주소지를 둔 지하철 노선만 가져오기 분류 함수
#subway_all_file()   # 전체 서울승하차 파일 합치기
#gu_corona()         # 자치구별 확진자 발생동향 시각화 나중에 자치구별 합쳐서 전체로 사용
#gu_gu()             # 자치구별로 서울승하차인원 파일 분류
#gu_subway()          # 최종 자치구별 서울승하차인원 분류 후 시각화까지
last_subway_corona()

# %%
