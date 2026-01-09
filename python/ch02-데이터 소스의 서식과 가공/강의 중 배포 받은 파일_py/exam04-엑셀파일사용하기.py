# 엑셀 파일 사용하기
# 많은 회사에서 엑셀 형식의 데이터를 배포하고 있으므로 파이썬으로 데이터를 수집했을 때 엑셀 파일로
# 읽고 쓸 수 있어야 한다. 파이썬에서 엑셀 파일을 읽고 쓸 때는 openpyxl 라이브러리를 사용한다.
# ch03에서 오른쪽 마우스 버튼을 눌러 컨텍스트 메뉴에서 Git Bash here를 클릭한다.
# Git Bash에서 'pip3 install openpyxl'을 입력하고 [Enter]키를 눌러 설치한다.

# 파이썬에서 엑셀 파일 읽기
# 국가 지표 체계에서 제공하는 자치단체 행정구역 및 인구 현황 엑셀 파일을 사용한다.
# 인터넷에서 '자치단체 행정구역 및 인구현황'로 검색하여 행정안정부의
# '행정동별 주민등록 인구현황'을 클릭하면 행정동별 연령별 인구현황을 조회하여 얻을 수 있다.
# status_104102.xlsx
# 엑셀에서는 엑셀 파일을 북(book)이라고 하고, 엑셀 파일에는 여러 개의 시트(sheet)가 있다.
# 각 시트는 행(row)과 열(column)을 가진 2차원 셀(cell)로 구성된다.


import openpyxl

# 엑셀 파일 열기 --- (※1)
filename = "stats_104102.xlsx"
book = openpyxl.load_workbook(filename)
# 엑셀(.xlsx) 파일을 열어서 워크북 객체로 로드한다.

# 맨 앞의 시트 추출하기 --- (※2)
sheet = book.worksheets[0]
# 엑셀 파일의 첫 시트를 추출한다.

# 시트의 각 행을 순서대로 추출하기 --- (※3)
data = [] # 빈 data 리스트를 선언한다.

for row in sheet.rows:
    data.append([row[0].value, row[10].value])
    # row[0](A열:지역), row[10](K열:2018년 인구수)의 값을 추출하여 data 리스트에 추가한다.

del data[0] # 헤더(제목) 행 제거
del data[1] # 연도 행 제거
del data[2] # 계 행 제거
# 필요없는 행(헤더, 연도, 계)을 제거한다.

data = sorted(data, key=lambda x:x[1])
# sorted(iterable, key=None, reverse=False)
# iterable(정렬할 대상 (리스트, 튜플, 문자열 등)), key(정렬 기준 함수 (옵션))
# reverse(True면 내림차순, 기본은 False(오름차순))
# 람다(lambda) 함수는 이름이 없는 함수로, 한 줄로 간단하게 정의할 수 있다.
# data를 두 번째 열(인구 수)의 값(x[1]) 기준으로 오름차순 정렬한다.
# 데이터를 인구가 작은 순서로 정렬한다.

# 위에서 다섯개를 출력한다.
for i, a in enumerate(data):
# enumerate(data) : 각 항목을 (index, value) 형태로 반환한다.
# i : 현재 항목의 인덱스 (0부터 시작), a : 현재 항목의 값(data)
    if (i >= 5): break # 인덱스 번호가 5 이상이면 프로그램을 종료한다.
    print(i+1, a[0], int(a[1]))
    # 인덱스 번호는 0번부터 시작하므로 +1을 한다.
    # a[0]은 도시명, a[1]은 인구수이다.




















