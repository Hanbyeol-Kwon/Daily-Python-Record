# Pandas(판다스)를 이용해 엑셀 파일 읽고 쓰기
# Pandas를 사용하면 엑셀을 쉽게 읽고 쓸 수 있다.

# Pandas 설치
# 명령 프롬프트에서 'pip install pandas'를 실행하여 설치한다.
# Pandas로 엑셀을 수정할 때 사용하는 xlrd 모듈을 설치한다.
# 명령 프롬프트에서 'pip install xlrd'를 실행하여 설치한다.
# 명령 프롬프트에서 'pip install openpyxl'를 실행하여 설치한다.


import pandas as pd

# 엑셀 파일 열기 --- (※1)
filename = "stats_104102.xlsx" # 파일 이름
sheet_name = "stats_104102" # 시트 이름
book = pd.read_excel(filename, sheet_name=sheet_name, header=1, engine='openpyxl')
# 첫 번째 줄부터 헤더

# 2018년 인구로 정렬 --- (※2)
book = book.sort_values(by=2018, ascending=False)

print(book)




















