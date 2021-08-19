# 문자 개수 세기(count)
a = "hobby"
print(a.count('b'))

# 위치 알려주기
a = "Python is the best choice"
print(a.find('b')) 
print(a.find('k')) # find 문은 문자가 없으면 -1 값을 출력
print(len(a))
print(a[0:15])

# 위치 알려주기 2
a = "Life is too short"
print(a.index('t'))
# print(a.index('k')) -> find 문과 다른 점은 문자가 없으면 오류 발생

# 문자열 삽입 ( join )
print(",". join('abcd'))
print(",". join(['a', 'b', 'c', 'd']))
print('a', 'b', 'c', 'd', sep=",")

# 소문자를 대문자로 바꾸기 (upper)
a = "hi"
print(a.upper())

# 대문자를 소문자로 바꾸기 (lower)
a = "HI"
print(a. lower())

# 왼쪽 공백 지우기 (lstrip)
a = " hi "
print(a.lstrip())

# 오른쪽 공백 지우기 (rstrip)
a = " hi "
print(a.rstrip())

# 양쪽 공백 지우기 (strip)
a = " hi "
print(a.strip())

# 문자열 바꾸기 (replace) 
a = "Life is too short"
print(a.replace("Life", "Your leg")) 

# 문자열 나누기 (split)
a = "Life is too short"
print(a.split()) # -> 공백을 기준으로 문자열 나눔

b = "a:b:c:d"
print(b.split(':'))

# 리스트의 인덱싱
a = [1, 2, 3]
print(a[0])
print(a[1])
print(a[2])
print(a[0] + a[2])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3])

print(a[-1][2])
print(a[-1][1])
print(a[3][0])

# 삼중 리스트에서 인덱싱하기
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])

# 리스트의 슬라이싱
a = [1,2,3,4,5]
print(a[0:2])
a = "12345"
print(a[0:2])

a = [1, 2, 3, 4,5]
b = a[:2]
c = a[2:]
print(b)
print(c)

# A = [1, 2, 3, 4, 5] 리스트에서 슬라이싱 기법을 사용하여 리스트 [2,3]을 만들어보자
test = [1, 2, 3, 4, 5]
print(test[1:3])

# 중첩 된 리스트에서 슬라이싱하기
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])

# 리스트 연산하기
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

a = [1, 2, 3]
print(a * 3)

a = [1,2,3]
print(len(a))

# 초보자가 실수하기 쉬운 리스트 연산 오류
a = [1, 2, 3]
print(str(a[2]) + "hi")

# 리스트에서 값 수정하기
a = [1, 2, 3]
a[2] = 4
print(a)

# del 함수 사용해 리스트 요소 삭제하기
a = [1, 2, 3]
del a[1]
print(a)

# 슬라이싱 기법을 사용하여 리스트의 요소 여러 개를 한꺼번에 삭제
a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

# 리스트에 요소 추가 (append)
a = [1, 2, 3]
a.append(4)
print(a)
a. append([5, 6])
print(a)

# 리스트 정렬 (sort)
a = [1, 4, 3, 2]
a. sort()
print(a)

a = ['a', 'c', 'e', 'd',]
a. sort()
print(a)

# 리스트 뒤집기 (reverse) 
a = ['a', 'c', 'b']
a. reverse()
print(a)

# 위치 반환 (index)
a = [1, 2, 3]
print(a.index(3)) # 3은 리스트 a의 세번째 (a[2])의 요소
print(a.index(1))
# print(a.index(0)) 0은 존재하지 않는 값으로 오류 발생

# 리스트에 요소 삽입 (insert)
a = [1, 2, 3]
a.insert(0, 4)
print(a)

a.insert(3, 5)
print(a)

# 리스트 요소 제거 (remove)
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
a.remove(3)
print(a)

# 리스트 요소 끄집어 내기 (pop) / pop은 리스트 맨 마지막 요소를 돌려주고 그 요소는 삭제한다
a = [1, 2, 3]
a.pop()
print(a)

a = [1, 2, 3]
a.pop(1)
print(a)

# 리스트에 포함된 요소 x의 개수 세기 (count)
a = [1, 2, 3, 1]
print(a. count(1))

# 리스트 확장 (extend)
a = [1, 2, 3]
a. extend([4, 5])
print(a)

b = [6, 7]
c = [8, 9]
a.extend(b)
a.extend(c)
print(a)