# chapter03-3 
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])


# 리스트 연산
print('>>>>>>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0])) # 문자 + 숫자는 불가하므로 str으로 형변환

# 값 비교
print(c == c[:3] + c[3:])
print()

# Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print('>>>>>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # [['a', 'b', 'c']] -> 리스트 안에 리스트
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[2] # 삭제
print('c - ', c)
print()

# 리스트 함수
a = []
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(10) # 끝에 숫자를 추가할 떄 append 사용
print('a - ', a)
a.sort() # 오름차순 정렬
print('a - ', a)
a.reverse() # 역순으로 
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7) # 2번쨰 위치에 7을 삽입할거야
print('a - ', a)
a.reverse()
print('a - ', a)
a.remove(10) # 원하는 숫자를 제거 할 때 사용 
print('a - ', a)
print('a - ', a.pop()) # pop은 마지막에 있는 원소를 출력한 뒤 제거 
print('a - ', a) # 제거 된 원소 나머지 원소 출력
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4)) # 내가 원하는 값이 이 안에 몇 개나 중복되어 있는지 / 정말 많이 쓰는 함수
ex = [8, 9]
a.extend(ex) # 확장
print('a - ', a)

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)
























