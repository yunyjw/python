# 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
# letters = 'python' / 실행 예 : p t
# 파이썬 문자열에서 한 글자를 가져오는 것을 인덱싱이라고 부릅니다. 파이썬 인덱싱은 0부터 시작합니다.
letter = 'python'
print(letter[0], letter[2])

# 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
# license_plate = "24가 2210"
license_plate = "24가 2210"
print(license_plate[-4:])
print(license_plate[4:8])

# 문자열 인덱싱
# 아래의 문자열에서 '홀'만 출력하세요
# 슬라이싱할 때 시작인덱스:끝인덱스:오프셋을 지정할 수 있습니다.
string = "홀짝홀짝홀짝"
print(string[::2])

# 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요

string = 'Python'
print(string[::-1])

# 문자열 치환
# 파이썬 문자열에서 replace 메서드를 사용하면 문자열을 일부를 치환할 수 있습니다.
# 문자열은 수정할 수 없는 자료형이므로 기존 문자열은 그대로 두고 치환된 새로운 문자열이 리턴됩니다.
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)

# 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
phone_number2 = phone_number.replace("-", "")
print(phone_number2)

# 문자열은 immutable / 아래 코드의 실행 결과를 예상해보세요.
# lang = 'python'
# lang[0] = 'P'
# print(lang)
# 문자열은 수정할 수 없습니다. 실행 결과를 확인해보면 문자열이 할당(assignment) 메서드를 지원하지 않음을 알 수 있습니다.

# replace 메소드-1
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'
string1 = string.replace('a', 'A')
print(string1)

# replace 메소드-2
# 아래 코드의 실행 결과를 예상해보세요.
# string = 'abcd'
# string.replace('b', 'B')
# print(string)

