import re

pattern = re.compile("ca.e")
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case ... | caffe
# ^ (^de) : 문자열의 시작 > desk, destination ... | fade
# $ (se$) : 문자열의 끝 > case, base ... | face

def print_if_match(val):
    if val:
        print("val.group() :", val.group()) # 일치하는 문자열 반환 // 매치되지 않았는데 이 명령문이 수행되면 오류 발생
        print("val.string :", val.string) # 입력받은 문자열 출력
        print("val.start() :", val.start()) # 일치하는 문자열의 시작 index
        print("val.end() :", val.end()) # 일치하는 문자열의 끝 index
        print("val.span() :", val.span()) # 일치하는 문자열의 시작과 끝 index

    else:
        print("매칭되지 않음")

val1 = pattern.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인 (뒷부분에 다른 문자열이 이어져 있어도 상관X)
print_if_match(val1)

val2 = pattern.search("good care") # search : 주어진 문자열 중에 일치하는 게 있는지 확인
print_if_match(val2)

val3 = pattern.findall("careless cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
print(val3)


# 1. p = re.complie("원하는 형태") : 원하는 형태는 정규식을 의미함
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중 일치하는 게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 문자열을 리스트 형태로 반환