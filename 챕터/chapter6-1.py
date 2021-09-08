# chapter6-1
# 파이썬 클래스
# OOP ( 객체 지향 프로그래밍 ), Self -> 인스턴스화 된 대상, 인스턴스 메소드 -> self를 인자로 받는 것들, 인스턴스 변수 -> self를 붙이고 선언하는 변수

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장 된 공간 - 자기만의 공간
# 클래스 변수 : 직접 접근 가능, 공유 - 모든 클래스, 모든 인스턴스 공유 속성
# 인스턴스 변수 : 객체마다 별도 존재 

# 예제 1


class Dog2:      # class Dog(object)로 표현 해도 됨 or class Dog()-> object 상속 받음
    # 클래스 속성
    species = 'firstdog' # 클래스 변수

    # 초기화/인스턴스 속성
    def __init__(self, name, age): # 클래스가 초기화 될 떄 반드시 호출 되어야 하는 함수 __init__(self, 변수1, 변수2) -> self는 자동으로 넘어옴
        self.name = name # 인스턴스 변수
        self.age = age

        # 소프트웨어를 구현할 대상을 객체라고 말함
        # 인스턴스는 코드에서 사용하는 어떤 객체

# 클래스 정보
print(Dog2)

# 인스턴스화 -> 설계로를 바탕으로 구현 된 것을 인스턴스화 되었다고 한다.
a = Dog2('natae', 2)
b = Dog2('Dongkyung', 3)

# 비교
print(a == b, id(a), id(b)) # 인스턴스화 된 객체들은 다 값이 다르다

# 네임스페이스 -> 클래스가 갖고 있는 속성들을 확인 할 수 있다.
print('dog1', a.__dict__)
print('dog1', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age)) 

if a.species == 'firstdog':
    print('{0} is a {1}'. format(a.name, a.species))

print(Dog2.species)
print(a.species)
print(b.species)

# 예제 2
# self의 이해
class SelfTest:
    def func1():
        print('Func1 called')
    def func2(self):
        print(id(self))
        print('Func2 called')

f = SelfTest()

# print(dir(f))  -> f안에 있는 모든 메소드 조회
print(id(f))
# f.func1() # 예외 발생
f.func2()

SelfTest.func1()
# SelfTest.func2() # 예외 발생
SelfTest.func2(f)

# 클래스 메소드는 클래스를 직접 호출
# self가 붙은거는 인스턴스 메소드여서 인스턴스를 넘겨주던가 인스턴스로 호출해야함

# 예제 3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수 = 0
    stock_num = 0 # 재고

    def __init__(self, name):
        # 인스턴스 변수 ( self가 붙은것을 인스턴스 변수라고 함 )
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num)

# 인스턴스 namespace에 없으면 class namespace에서 찾아보고 출력

del user1
print('after', Warehouse.__dict__)

# 예제 4
class Dog:      # class Dog(object)로 표현 해도 됨 or class Dog()-> object 상속 받음
    # 클래스 속성
    species = 'firstdog' # 클래스 변수

    # 초기화/인스턴스 속성
    def __init__(self, name, age): # 클래스가 초기화 될 떄 반드시 호출 되어야 하는 함수 __init__(self, 변수1, 변수2) -> self는 자동으로 넘어옴
        self.name = name # 인스턴스 변수
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)

# 인스턴스 생성
c = Dog('Natae', 4)
d = Dog('Dongkyung', 10)

# 메소드 호출
print(c.info())
print(d.info())
# 메소드 호출
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))