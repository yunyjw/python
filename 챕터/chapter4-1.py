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
