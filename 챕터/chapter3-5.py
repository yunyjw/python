# chapter3-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형 (순서X, 키 중복X, 수정O, 삭제O)

# 선언  # 어떤 자료형도 key가 될 수 있음 ( int, str-일반적 사용 )
a = {'name': 'kim', 'phone': '01033336777', 'birth': '951127'}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 27,
    'Grade': 'A',
    'Status': True
}
e = dict([
    ('Name', 'Niceman'),
])

# 많이 사용하는 방식
f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

# 출력
print('a - ', a['name']) # key가 존재하지 않으면 error 발생
print('a - ', a.get('name')) # get 함수는 key가 없는 값이면 none으로 출력 됨
print('b -', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f['Age'])

# 딕셔너리 길이
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)
print('a - ', len(a))
print('a - ', len(b))
print('a - ', len(c))
print('a - ', len(d))

# dict_keys, dict_values, dict_items : 반복문(__itter__)에서 사용 가능

print('a - ', a.keys()) # 키 값들만 출력 하는 함수
print('a - ', b.keys())
print('a - ', c.keys())
print('a - ', d.keys())
print('a - ', list(a.keys())) # 리스트로 형 변환
print()

print('a - ', a.values()) # 값만 나오게 하는 함수
print('a - ', list(a.values()))
print()

print('a - ', a.items()) # 키와 값을 모두 나오게 하는 함수
print('a - ', b.items())
print('a - ', list(c.items()))
print()

print('a - ', a.pop('name'))
print('a - ', a)
print()

print('a - ', c.pop('arr'))
print('a - ', c)
print('a - ', d.pop('Name'))
print('a - ', d.pop('Age'))
print('a - ', d)
print()

print('f - ', f.popitem()) # 아무거나 하나를 임의로 갖고 와서 지움
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print()

# 키를 조회할 때 in 명령어로 해당 키가 있는지 조회함
print('a - ', 'birth' in a)
print('a - ', 'city' in d)

# 수정
a['test'] = 'test_dict'
print('a -', a)

a['address'] = 'dj'
print('a - ', a)

a.update(birth='910904')
print('a - ', a)
temp = {'address': 'Busan'}

a.update(temp)
print('a - ', a)

