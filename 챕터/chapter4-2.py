# chapter4-2 
# 파이썬 반복문
# FOR 실습

# 코딩의 핵심
# for in <collection>
# < Loop body >

for v1 in range(10): # 0 ~ 9
    print('v1 is :', v1)
print()

for v2 in range(1, 11): # 1 ~ 10
    print('v2 is :', v2)
print()

for v3 in range(1, 11, 2): # 2개씩 호출
    print('v3 is :', v3)
print()
# 1 ~ 1000합

sum1 = 0

for v in range(1, 1001):
    sum1 += v      # sum1 = sum1 + v
print('1 ~ 1000 sum : ', sum1)

print('1 ~ 1000 Sum : ', sum(range(1, 1001)))

print('1 ~ 1000 4의 배수의 합 : ', sum(range(4, 1001, 4)))

# Iterables 자료형 반복 
# interable : 한 번에 하나의 member를 반환할 수 있는 object (객체)를 의미.
# 문자열, 리스트, 튜플, 집합, 딕셔너리
# Iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제 1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for name in names:              # for 뒤에는 별칭으로 아무거나 적어도 되고 위에 선언한 변수를 뒤에 잘 적어주면 된다.
    print('You are : ', name)

# 예제 2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print('Current Number :', n)

# 예제 3
word = 'Beautiful'

for s in word:
    print('word : ', s)

# 예제 4
my_info = {
    "name": 'Lee',
    'Age': '33',
    'City': 'Seoul'
}

for k in my_info:
    #print('key :', my_info.get(k))
    print('key :', my_info[k])
    #print('key :', k)
#for v in my_info.values():
    #print('value :', v)
print()

# 예제 5 -> 모든 문자를 대문자로 출력
name = 'FineAppLE'

for n in name:
    if n.isupper():     # isupper 대문자 / islower 소문자
        print(n)
    else:
        print(n.upper())

# 예제 6 / break -> 불필요한 반복문 종료
# numbers 리스트 중 34를 찾으면 그 반복문을 종료해라
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 39]

for num in numbers:
    if num == 34:
        print('Found : 34!')
        break
    else:
        print('Not Found :', num)

# continue -> 많은 데이터 중에 보기 싫은 또는 불필요한 계산값이 있을 때 continue를 써서 패스할 수 있음

lt = ["1", 2, True, 4.3, complex(4)]

# 타입이 bool이고 continue를 만나면 아래 명령을 실행하지 않음
for v in lt:
    if type(v) is bool:             # 자료형을 대조할 땐 is를 사용
        continue
    print("current type: ", v, type(v))
    print('multiply by 2: ', v * 3)

# for - else
# 모든 원소를 반복했을 때 else 문을 수행한다 / break문 또는 위에서 종료되면 else는 실행 안됨

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 39]

for num in numbers:
    if num == 24:
        print('Found : 24')
        break
else:
    print('Not Found : 24')

# 구구단 출력

for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i * j), end = '')  # 4자리의 정수형으로 출력
    print()

# 변환 예제
name2 = 'Aceman'

print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2))) # 집합은 순서가 없음 - 무작위


