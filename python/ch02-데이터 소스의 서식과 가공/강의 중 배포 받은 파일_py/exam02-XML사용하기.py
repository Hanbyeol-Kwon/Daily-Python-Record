# XML(Extensible(익스텐서블,확장성 있는) Markup Language) 사용하기
# 데이터를 계층 구조로 표현할 수 있으며, 어떤 데이터 아래에 서브 데이터를 추가할 수 있다.
# 범용적인 형식으로 웹 API에서 XML 형식을 활용한다. 다음은 일반적인 형식이다.
# 데이터를 태그로 감싸 마크업한다.
'''
    <products type="전자제품">
        <product id="S001" price="45000">SD 카드</product>
        <product id="S002" price="12000">마우스</product>
    </products>
'''

# 파이썬으로 XML 분석하기
# 기상청 에서 공개한 XML 형식의 데이터를 읽고, 현재 지역의 날씨를 분류한다.
# http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108
# XML 형식의 데이터를 읽고, 현재 지역의 날씨를 분류하는 프로그램을 만들어 보자.
# XML 데이터를 내려받아 현재 날씨를 분석하고 분류한다.
# 현재 기상청 서비스는 중단 상태이므로 제공한 forecast.xml 파일을 사용한다.


from bs4 import BeautifulSoup 
import urllib.request as req
import os.path

'''
# 가상청 날씨누리 기상청 RSS에서 중기 예보의 전국 버튼을 눌러 웹주소를 얻는다.
url = "https://www.weather.go.kr/plus/rss/mid-term-rss3.jsp?stnId=108"
'''
savename = "forecast.xml"
'''
# XML 데이터를 forecast.xml 파일로 다운하기 --- (※1)
if not os.path.exists(savename):
    req.urlretrieve(url, savename)
# os.path.exists(savename)는 savename에 저장된 파일이 존재하면 true, 존재하지 않으면
# false를 반환한다. 폴더와 파일의 유무를 체크하여 파일이 모두 다운됐는지 확인한다.
# urllib.request 모듈에 있는urlretrieve()로 파일을 다운로드한다.
# retrieve(릿리브:찾아서 얻는다)
# urlretrieve()의 첫번째 매개값은 다운로드 받을 파일의 URL을 지정한다.
# 두번째 매개값은 저장할 파일의 경로를 지정한다.
# 프로그램을 실행할 때마다 XML 파일을 내려받으면, 서버에 부하를 줄 수 있으므로
# XML 파일로 데이터를 저장한 후 실행할 때 저장한 데이터를 읽어 사용한다.
'''

# XML 파일에서 데이터를 읽고 BeautifulSoup로 XML 분석하기 --- (※2)
xml = open(savename, "r", encoding="utf-8").read()
# forecast.xml 파일을 가져온다.
# open(파일경로, 파일모드 , 인코딩방식), 다운로드 받은 XML 파일을 열어 내용을 문자열로 얻는다.
# XML 파일의 저장 위치(savename), 파일모드는 읽기모드( r ) , 인코딩 방식은 utf-8로 지정한다.
# read()로 파일을 읽고, 읽은 데이터(문자열)를 xml 에 저장한다.

soup = BeautifulSoup(xml, 'html.parser')
# BeautifulSoup 객체를 생성하고, xml을 분석한다.
# 첫번째 매개값으로 분석할 대상을 지정하고, 두번째 매개값으로 분석할 분석기(parser)의 종류를 지정한다.
# xml을 분석할 때는 'html.parser'로 지정한다.


# 각 지역 확인하기 --- (※3)
# BeautifulSoup 객체의 find(), find_all() 등을 활용하여 원하는 요소를 선택한다.
info = {}
# 날씨 상태별로 도시명을 저장할 빈 딕셔너리를 생성한다.

for location in soup.find_all("location"):
    # 반복하여 모든 location 요소를 선택한다.
    name = location.find('city').string
    # location 요소의 하위 요소인 city 요소를 선택하여 데이터(도시명)를 얻는다.
    weather = location.find('wf').string
    # location 요소의 하위 요소인 wf 요소를 선택하여 데이터(날씨상태)를 얻는다.
    
    if not (weather in info): # 날씨 상태가 딕셔너리에 없으면
        info[weather] = [] # 빈 리스트로 초기화한다.
        
    info[weather].append(name) # info-딕셔너리형인데, 내부에 리스형을 키로 가진다.  
    # 날씨 상태에 해당하는 도시명을 리스트에 추가한다.

# info 딕셔너리는 날씨 상태를 key로 하고, 날씨를 가진 도시들의 리스트를
# value로 가진다. 즉, 날씨별로 도시들을 분류하는 딕셔너리를 만든다.
'''
{
    "맑음": ["서울", "부산", "대전"],
    "흐림": ["광주", "인천"],
    "비": ["제주"]
}
'''


# 각 지역의 날씨를 구분해서 출력하기 --- (※4)
for weather in info.keys():
# info 딕셔너리의 모든 날씨 상태(key)를 반복한다.
    print("+", weather) # 날씨 상태를 출력한다.
    for name in info[weather]:
    # 날씨 상태에 속한 도시 리스트를 반복한다.
        print("| - ", name) # 도시명을 출력한다.