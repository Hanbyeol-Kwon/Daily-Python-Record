# 엑셀 파일 쓰기
# 각 연도의 인구 합계에서 서울 인구를 제외한 인구수를 B21 ~ K21에 작성하는 프로그램을 만든다. 

import openpyxl

# 엑셀 파일 열기 --- (※1)
filename = "stats_104102.xlsx"
book = openpyxl.load_workbook(filename)
# 엑셀(.xlsx) 파일을 열어서 워크북 객체로 로드한다.


# 활성화된 시트 추출하기 --- (※2)
sheet = book.active


# 서울을 제외한 인구의 합계를 얻어서 쓰기 --- (※3)
for i in range(0, 10): # 0부터 9까지 정수를 생성한다.
# range(start, stop, step) : start(시작값), stop(끝값), step(증가폭)
# start부터 end 이전까지 정수를 생성한다. i 는 0부터 9까지의 값을 가진다.
    total = int(sheet[str(chr(i + 66)) + "3"].value)
    # 66은 ASCII 코드로 'B'에 해당하며, chr(i + 66)는 'B', 'C', 'D' ...
    # str(chr(i + 66)) + "3" : 'B' + '3'은 'B3'이다.
    # 엑셀 파일의 열 문자를 동적으로 선택할 때 사용한다.
    seoul = int(sheet[str(chr(i + 66)) + "4"].value)
    # 'B4', 'C4', 'D4', 'E4', 'F4' ... 'K4'
    output = total - seoul
    # 전체 인구수에서 서울 인구수를 제외한 인구수를 구한다.
    print("서울 제외 인구 =", output)
    
    # 전체 인구수에서 서울 인구수를 제외한 인구수를 B21 ~ K21에 쓰기 --- (※4)
    sheet[str(chr(i + 66)) + "21"] = output
    cell = sheet[str(chr(i + 66)) + "21"]
    
    # 폰트와 색상 변경해보기 --- (※5)
    cell.font = openpyxl.styles.Font(size=14,color="FF0000")
    cell.number_format = cell.number_format
    # cell.number_format은 셀의 숫자/날짜 표시 형식(format)으로 변경된 출력 형식을 할당하여
    # 출력 형식을 변경한다.


# 엑셀 파일 저장하기 --- (※6)
filename = "population.xlsx"
book.save(filename) # 파일을 저장한다.
print("Write Success!")




















