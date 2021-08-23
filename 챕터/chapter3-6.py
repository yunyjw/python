# chapter3-6
# 집합(Set) 특징
# 집합(Set) 자료형(순서X, 중복X)

# 선언
a = set()
b = set([1, 2, 3, 4, 4, 4, 4]) # 중복을 허용하지 않아서 4는 한개만 출력 됨
c = set([1, 4, 6, 7])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'} # key와 values가 없다면 딕셔너리가 아닌 집합(Set)
f = {42, 'foo', (1, 2, 3), 3.1414142}

print('a - ', type(a), a) 
print('a - ', type(b), b)
print('a - ', type(c), c)
print('a - ', type(d), d)
print('a - ', type(e), e)
print('a - ', type(f), f)

# 튜플 변환(set -> tuple)
t = tuple(b)
print('t - ', t)
print(type(t))
print('t - ', t[0], t[1:3])
print()

# 리스트 변환(set -> list)
l = list(c)
l2 = list(e)

print('l - ', l)
print('l2 -', l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6])

print('s1 & s2 : ', s1 & s2) # s1과 s2의 교집합을 보여줘
print('s1 & s2 : ', s1.intersection(s2)) # 함수로 쓰려면 intersection(교차) 사용

print('s1 | s2 : ', s1 | s2)
print('s1 | s2 : ', s1.union(s2)) # 함수로 쓰려면 union 사용

print('s1 - s2 : ', s1 - s2)
print('s1 - s2 : ', s1.difference(s2)) # 함수로 쓰려면 difference 사용

# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2)) # false가 나오면 교집합 되는 부분이 있다 없으면 true / dis가 붙었기에 반대로 나오는것

# 부분 집합 확인
print('subset : ', s1.issubset(s2)) # s1이 s2의 부분집합이냐
print('superset : ', s1.issuperset(s2)) # s1이 s2를 포함하는 부분집합이냐

# 추가 & 제거
s1 = set([1, 2, 3, 4])

s1.add(5)
print('s1 - ', s1)

s1.remove(2) # 없는 값을 지우면 keyerror 발생
print('s1 - ', s1)

s1.discard(3)
print('s1 - ', s1)

'''
s1.discard(7)
print('s1 - ', s1) # 7이라는 값이 없어도 에러가 발생하지 않음
'''

s1.clear() # clear 명령어를 사용하면 전부 다 지워짐
print('s1 - ', s1) 

a = [1, 2, 3]
a.clear()
print(a)
