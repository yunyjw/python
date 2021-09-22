# chapter8-1
# 파이썬 내장(Built-in) 함수
# 자주 사용하는 함수 위주로 실습
# 사용하다보면 자연스럽게 숙달
# str(), int(), tuple() 형변환 이미 학습

# 절대값
# abs() 모든 언어에 다 있음

print(abs(-3))

# all, any : iterable 요소 검사 (참, 거짓)
print(all([1,2,3,0]))  # 하나라도 false 값이 있으면 false 출력 = and
print(any([1,2,0])) # 하나라도 true 값이 있으면 true 출력 = or 

# chr : 아스키 -> 문자, ord : 문자 -> 아스키

print(chr(44))
print(chr(67))
print(ord('C'))

# enumerate : 인덱스 + Iterable 객체 생성 / 필수
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i, name)

# filter : 반복 가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출 / 필수

def conv_pos(x):
    return abs(x) > 2 # 절대값 2보다 큰 값만 가져오겟다

print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))  # list형 변환 하여 리스트 출력
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6])))  # lambda는 함수를 딱 한줄만으로 만들게 해주는 역할

# id : 객체의 주소값 ( 레퍼런스 ) 반환
print(id(int(5)))
print(id(4))

# Len : 요소의 길이 반환
print(len('abcdefg'))
print(len([1,2,3,4,5,6,7]))

# max, min : 최대값, 최소값

print(max([1, 2, 3]))
print(max('python study'))
print(min([1, 2, 3]))
print(min('pythonstudy'))  # 공백이 있으면 최소값으로 찍힘

# map : 반복 가능한 객체 요소를 지정한 함수 실행 후 추출 / 필수
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [1, -3, 2, 0, -5, 6])))
print(list(map(lambda x: abs(x), [1, -3, 2, 0, -5, 6])))

# pow : 제곱값 반환
print(pow(2, 10))

# range : 반복 가능한 객체(Iterable) 반환
print(list(range(1, 10, 2)))
print(list(range(0, -15, -1)))

# round : 반올림
print(round(6.64532, 2)) # 소수점 둘쨰자리에서 반올림해라
print(round(5.4)) # 두번쨰 인자를 넣지 않으면 첫째자리에서 반올림 함

# sorted : 오름차순 / 반복 가능한 객체(Iterable)를 정령 후 반환
print(sorted([6,7,8,34,32,1])) 
print(sorted(['p', 'y', 't', 'h', 'o', 'n']))

# sum : 반복 가능한 객체(Iterable) 합 반환
print(sum([6,7,8,9,10]))
print(sum(range(1, 101)))

# type : 자료형 확인
print(type(3))
print(type({}))
print(type({3, 4}))  # key, value 있으면 셋
print(type(()))
print(type([]))

# zip : 반복 가능한 객체 (Iterable)의 요소를 묶어서 반환
print(list(zip([10,20,30], [40,50,60])))  # 짝이 없으면 못묶어서 반환 x 
print(zip([10,20,30], [40,50,60])) # 리스트가 없으면 object가 보임
print(type(list(zip([10,20,30], [40,50,60]))[0]))