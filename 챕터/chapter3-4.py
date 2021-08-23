# chapter03-4
# 파이썬 튜플 / ()로 표기되면 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서O, 중복O, 수정X, 삭제X) / 불변 - 절대 변경되면 안되는 값들 지정

a = ()
b = (1,) # 튜플로 인식할 때는 꼭 ,로 끝나야함 / ,를 찍지 않으면 정수형으로 인식함
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('>>>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1])
print('d - ', e[-1][1])
print('d - ', list(e[-1][1])) # 튜플 -> 리스트로 형 변환

# 수정 x
# d[0] = 1500 -> 수정 안됨

# 슬라이싱
print('>>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[2][1:3])

# 튜플 연산
print('>>>>>>>>')
print('c + d', c + d)
print(' c * 3', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3)) # 숫자 3이 들어있는 위치가 어디냐
print('a - ', a.count(2)) # 숫자 2가 몇개 들어있냐

# 팩킹 & 언팩킹(Packing, and Unpacking) - 파이썬의 특징에서 중요함

# 팩킹 == 묶다
t = ('foo', 'bar', 'baz', 'qux')

print(t)
print(t[0])
print(t[-1])

# 언팩킹1 ( 각각 묶여있는걸 하나하나 푸는걸 언팩킹이라고 함 )
(x1, x2, x3, x4) = t # 괄호가 없더라도 언팩킹이 이루어지지만 관습상 사용하는 문법

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)
print()

# 팩킹 & 언팩킹
t2 = (1, 2, 3)
t3 = (4)
x1, x2, x3 = t2
x4, x5, x6 = (4, 5, 6)

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
print(type(t2))


