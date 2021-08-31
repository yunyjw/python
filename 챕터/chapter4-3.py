# chapter4-3
# 파이썬 반복문
# while문

# whlter <expr>:
#    <statement(s)>

# 예제 1

n = 5
while n > 0: # n이 0보다 클 때 까지
    n = n -1 
    print(n)
print()

# 예제 2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop(-1)) # pop은 끝에꺼 하나를 꺼내오고 지움
    # print(a.pop()) -1이나 공백이나 같은 값 출력

# if 중첩
# 예제 3
# break, continue

n = 5
while n > 0:
    n -= 1      # n에서 1을 빼준다
    if n == 2:  # n이 2일 때는 break
        break
    print(n)
print('Loop Ended.')

# 예제 4
m = 5
while m > 0:
    m -= 1      # n에서 1을 빼준다
    if m == 2:  # n이 2일 때는 break
        continue
    print(m)
print('Loop Ended.')


# 예제 5

i = 1
while 1 <= 10:
    print('i : ', i)
    if i == 6:
        break
    i += 1

# while - else 구문
# 예제 6

n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:           # break가 없다면 else 문이 실행 됨
    print('else out.')      # 마지막에 실행되어야 하는 코드를 적어준다고 생각해라

# 예제 7
a = ['foo', 'bar', 'baz', 'qux']
s = 'kim'

i = 0 
while i < len(a):  # i 가 4 미만일 때랑 같은 의미
    if a[i] == s:   # a의 인덱스 0, 1, 2, 3이 s와 같을 때
        break
    i += 1
else:
    print(s, 'not found in list') # 찾았기 때문에 break문이 실행 안됨

# 무한 반복
# while True:
#    print('Foo')

# 예제 8
a = ['foo', 'bar', 'baz']

while True:     # while 에 트루문을 쓰고 싶을 때
    if not a:       # a가 false ( 비어있는 값이면 ) break 실행 
        break       # 4번째 실행될 때 값이 없기 떄문에 break 실행 됨
    print(a.pop())