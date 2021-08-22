# chapter3-2
# 파이썬 문자형
# 문자형 중요 !

# 문자열 생성
str1 = "I am Python"
str2 = "Python"
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4)) # len은 문자열의 길이를 뜻함 length 

# 빈 문자열
str1_t1 = ""
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
# I'm Boy 
"""
참고 : Escape 코드
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : null 문자
...
"""

print("I'm Boy")
print('I\'m Boy') # '' 안에 '를 사용하고 싶으면 \ 기호를 사용

print('a \t b')  # \t 는 키보드 탭키만큼 간격 벌어짐
print('a \n b') # \n은 줄 바꿈을 의미
print('a \"\" b') 

escape_str1 = "Do you have a \"retro game\"?"
print(escape_str1)
escape_str2 = 'Hi Hello World \'korea\''
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)

# Raw String 출력
raw_s1 = r'D:\python\test' # 드라이브 경로에 파일을 복사하거나 쓸 때 사용

print(raw_s1)
print()

# 멀티라인 입력 -> \ 끝나면 파이썬은 다음에 어떤 변수를 바인딩하는구나 라고 인식함
multi_str = \
'''
문자열
멀티라인 입력
테스트
'''

print(multi_str)


# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('z' in str_o1)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)
print("Capitalize: ", str_o1.capitalize()) # 대문자로 변경
print("endswitch?: ", str_o2.endswith("e")) # 마지막 문자가 뭐인지 체크
print("replace", str_o1.replace("thon", " Good")) # thon이라는 문자를 Good으로 바꿔줘
print("sorted: ", sorted(str_o1)) # 리스트 형태로 반환
print("split: ", str_o4.split(" ")) # 특정 단어를 분리할 때 ( 현재는 공백이기에 공백으로 확인 )

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) # __iter__

# 출력
for i in im_str:
    print(i)

# 슬라이싱 
str_sl = "Nice Python"

print(len(str_sl))

# 슬라이싱 연습
print(str_sl[0:3]) # 마지막에 -1까지 나옴 / 결론 : 3-1 이기 때문에 0,1,2번 까지 나옴
print(str_sl[5:])  # 5부터 끝까지 가져와 -> 끝 숫자 지정 안하고 공백일 때
print(str_sl[:len(str_sl)]) # str_sl[:11] -> 처음부터 11까지를 의미(len 함수로 전체길이를 삽입)
print(str_sl[:len(str_sl)-1])
print(str_sl[1:9:2]) # 2칸마다 출력
print(str_sl[-5:]) # 뒤에 -5칸부터 출력해라
print(str_sl[1:-2])
print(str_sl[::2])
print(str_sl[::-1])

# 아스키 코드 (또는 유니코드)
a = 'z'
print(ord(a)) # 아스키 코드로 
print(chr(122)) # 문자로 




















