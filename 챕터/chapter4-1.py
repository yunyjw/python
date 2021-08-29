# chapter4-1
# 파이썬 제어문
# IF 실습

# 기본 형식
print(type(True)) # 0이 아닌 수, "abc", [1, 2, 3..], (1, 2, 3...) -> 무엇인가 존재 하는 수
print(type(False)) # 0, "", [], (), {} -> 빈 숫자

# 예제 1
if True: 
    print('good')

if False:
    print('bad')

# 예제 2
if False:
    print('bad!')
else:
    print('Good!')

# 관계 연산자
# >, >=, <, <=, ==, !=

# 예제 3

x = 15
y = 10

# 양변이 같은 경우 참
print(x == y)

# 양변이 같지 않은 경우 참
print(x != y)

# 왼쪽이 클 때 참
print(x > y)

# 왼쪽이 크거나 같을 때 참
print(x >= y)

# 오른쪽이 클 때 참
print(x < y)

# 오른쪽이 크거나 같을 때 참
print(x <= y )

# 예제 4
city = ""
if city:
    print("You are in:", city)
else:
    print("Please enter your city")

city = "Seoul"
if city:
    print("You are in:", city)
else:
    print("Please enter your city")

# 논리연산자(중요)
# and, or, not

a = 75
b = 40
c = 10

print('and:', a > b and b > c) # a > b > c
print('or:', a > b or b > c)
print('not:', not a > b) # not은 반대로 출력
print('not:', not b > c)
print(not True)
print(not False)

# 산술, 관계, 논리 우선순위
# 우선순위 : 산술 > 관계 > 논리
print('e1 :', 3+12 > 7+3)
print('e2 :', 5 + 10 * 3 > 7 + 3 * 20)
print('e3 :', 5 + 10 > 3 and 7 + 3 == 10) # 1번 계산 : 15가 3보다 크다, 2번 계산 : 7 + 3은 10과 같다 / True
print('e4 :', 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'

# 복수의 조건이 모두 참일 경우에 실행 == and
if score1 >= 90 and score2 == 'A':
    print('pass')
else:
    print('Fail')

# 예제 5
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')

if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')

# 예제 6
# 다중 조건문 : elif는 조건문을 계속 붙일 수 있다
num = 90

if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('과락')

# 예제 7
# 중첩 조건문 : if문 안에 if

grade = 'A'
total = 90

if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')

else:
    print('장학금 없음')

# in, not in
q = [10, 20, 30] # 리스트
w = {70, 80, 90, 100} # 집합
e = {"name": "Lee", "city": "Seoul", "grade": "A"} # 딕셔너리
r = (10, 12, 14) # 튜플

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)
print("Seoul" in e.values()) # valuse는 key는 버리고 값만 가져옴
