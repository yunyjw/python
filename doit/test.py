# 숫자 14를 3으로 나누었을 때 몫과 나머지를 확인해보자
print(14 // 3, 14 % 3)

head = "Python"
tail = " is fun!"
print(head + tail)

# You need python 문장을 문자열로 만들고 길이를 구해보자
a="You need python"
print(a, len(a))
print(type(a))

a="Life is too short, You need Python"
print(a[0], a[12], a[-1], a[-2], a[-5])

a="Life is too short, You need Python"
print(a[0:4], a[0:-1])

print(a[3:7], a[3:],)

print(a[:])

a = "20010331Rainy"
date = a[8:]
weather = a[:8]
print(date, weather)
print(len(a))

# Pithon 문구를 Python으로 바꾸려면? 
a= "Pithon"
print(a[:1], 'y', a[2:])
print(a[:1], end=""),print("y", end=""), print(a[2:])

string = "I eat %d apples." % 3
print(string)

string_1 = "I eat %s apples." % "five"
print(string_1)

number = 3
string_2 = "I eat %d apples." % number
print(string_2)

number, day = 10, "three" 

string_3 = "I ete %d apples. so I was sick for %s days." % (number, day)
print(string_3)

string_4 = "Error is %d%%." % 98
print(string_4)

print("%10s" % "hi")

print("%-10sjane" % "hi")

print("%0.4f" % 3.4123124124)
print("%10.4f" % 3.4234123412)

print("I eat {0} apples". format(3))
print("I eat {0} apples". format("five"))

number = 3
print("I eat {0} apples". format(number))

number, day = 10, "three"
print("I ate {0} apples. so I was sick for {1} days.". format(number, day))
print("I ate {number} apples. so I was sick for {day} days.". format(number = 10, day = "three"))
print("I ate {0} apples. so I was sick for {day} days.". format(10, day = "test"))

print("{0:<10}". format("hi"))
print("{0:>10}". format("hi"))
print("{0:^10}". format("hi"))
print("{0:!<10}". format("hi"))

y = 3.421321
print("{0:.>10.4f}". format(y))
print("{{and}}". format())

name, age = "홍길동", 30
print(f"'나의 이름은 {name}입니다. 나이는 {age}입니다.'". format(name, age))

age = 30
print(f"나는 내년이면 {age+1}살이 된다")

d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

print(f'{"hi":<10}')
print(f'{"hi":>10}')
print(f'{"hi":^10}')

print(f'{"hi":>5}')
print(f'{"hi":=^10}')
print(f'{"hi":!<10}')

y = 3.4215313
print(f'{y:0.4f}')
print(f'{y:10.4f}')

# format 함수 또는 f 문자열 포매팅을 사용해 '!!!python!!!' 문자열을 출력해 보자

print('{0:!^12}'. format("python"))
print(f'{"python":!^12}')