# 삼성전자라는 변수로 50,000원을 바인딩 해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

# 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩 해보세요.
"""
시가총액 298조
현재가 50,000원
PER 15.79
"""
시가총액 = "298조"
현재가 = 50000
PER = 15.79

print(시가총액, type(시가총액), 현재가, type(현재가), PER, type(PER))

# 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
s = "hello"
t = "python"
# 실행 예) hello! python
print(s + "!", t)

# type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.
"""
>> a = 128
>> print (type(a))
<class 'int'>

아래 변수에 바인딩된 값의 타입을 판별해보세요.
>> a = "132"
"""
a = "132"
print(type(a))

# 문자열 '720'을 정수형으로 변환해보세요.
num_str = "720"
num_int = int(num_str)
print(num_int, type(num_int))

# 정수를 문자열 100으로 변환
num = 100
num_str = str(num)
print(num_str, type(num_str))

# 문자열 "15.79"를 실수 타입으로 변환해보세요.
string_01 = "15.79"
num_float = float(string_01)
print(num_float, type(num_float))

# year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
year = "2020"

data = int(year)
print(int(data) - 1)
print(int(data) - 2)
print(int(data) - 3)

# 파이썬 계산
월 = 48584
총금액 = 월 * 36
print(총금액)