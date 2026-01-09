# JSON 사용하기
# JSON 소개 페이지 : http://json.org/
# JSON(JavaScript Object Notation, JavaScript 객체 표기법)은 경량 데이터 전달 형식이다.
# 기계가 쉽게 파싱하고 생성하며, 인간이 읽고 쓰는 것도 쉽다.
# JSON의 배열(Array)는 파이썬의 리스트와 같으며, JSON의 객체는 파이썬의 딕셔너리와 같다.

# 데이터는 'https://api.github.com/repositoryes' or
# 'https://api.github.com/users/octocat/repos'이다.

# 무작위로 리포지터리명과 소유자를 추출하여 출력한다.



import urllib.request as req
import os.path, random
import json


# 웹 API에서 JSON 데이터 내려받기 --- (※1)
url = "https://api.github.com/repositories"
savename = "repo.json"

if not os.path.exists(savename):
    req.urlretrieve(url, savename)
# os.path.exists(savename)는 savename에 저장된 파일이 존재하면 true,
# 존재하지 않으면 false를 반환한다. 폴더와 파일의 유무를 체크하여 파일이 모두 다운됐는지 확인
# urllib.request 모듈에 있는urlretrieve()로 파일을 다운로드한다.
# retrieve(릿리브:찾아서 얻는다)
# urlretrieve()의 첫번째 매개값은 다운로드 받을 파일의 URL을 지정한다.
# 두번째 매개값은 저장할 파일의 경로를 지정한다.
# 프로그램을 실행할 때마다 JSON 파일을 내려받으면, 서버에 부하를 줄 수 있으므로
# JSON 파일로 데이터를 저장한 후 실행할 때 저장한 데이터를 읽어 사용한다.


# JSON 파일 분석하기 --- (※2)
items = json.load(open(savename, "r", encoding="utf-8"))
# 또는
# s = open(savename, "r", encoding="utf-8").read()
# items = json.loads(s)

# repo.json 파일을 가져온다.
# open(파일경로, 파일모드 , 인코딩방식), 다운로드 받은 JSON 파일을 열어 내용을 문자열로 얻는다.
# JSON 파일의 저장 위치(savename), 파일모드는 읽기모드( r ) , 인코딩 방식은 utf-8로 지정한다.
# read()로 파일을 읽고, 읽은 데이터(문자열)를 s 에 저장한다.
# json.load()는 파일이 아닌 JSON 문자열을 얻는다.


# 출력하기 --- (※3)
for item in items:
    print(item["name"] + " - " + item["owner"]["login"])
    # name키에 해당하는 값을 출력한다. [ { ... "name":"rubinius" ... }, { ... }, ... ]
    # owner키에 해당하는 값 중에 login 키에 해당하는 값을 출력한다.
    # { ... "owner":{"login":"rubinius","id":317747,"node_id":"MDEy... ", ... }