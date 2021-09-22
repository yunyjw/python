# chapter8-2
# 파이썬 외장(External) 함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shutil, temfile, time, random 등

# 예제1
import sys
print(sys.argv)    # 파이썬 파일을 외부에서 실행할 때 어떤값들을 파이썬에 전달해서 값에 맞는 모드로 실행 시킬 수 있음

# 예제2 ( 강제 종료 )
# sys.exit() 

# 예제3(파이썬 패키지 위치)
print(sys.path)

# pickle : 객체 파일 읽기, 쓰기
import pickle 

# 예제4 (쓰기)
f = open("test.obj", 'wb')
obj = {1: 'python', 2: 'study', 3:'basic'}
pickle.dump(obj, f)  # 쓸 때는 dump
f.close()

# 예제5(읽기)
f = open('test.obj', 'rb')
data = pickle.load(f)  # 읽을 때는 load
print(data, type(data))
f.close()

# 예제6
# os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
import os
print(os.environ)
print(os.environ["USERNAME"])

# 예제7 (현재경로)
print(os.getcwd())

# 예제8
# time : 시간 관련 처리 / 중요
import time
print(time.time())

# 예제9 (형태변환)
print(time.localtime(time.time()))

# 예제10 (간단표현)
print(time.ctime())
print()

# 예제11 (형식표현)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 예제12 (시간 간격 발생)
# for i in range(5):
#     print(i)
#     time.sleep(1)

# random : 난수 리턴
import random

# 예제13
print(random.random()) # 0 ~ 1 실수

# 예제14
print(random.randint(1, 45))
print(random.randrange(1, 45))

# 예제15 (섞기)
d = [1,2,3,4,5]
random.shuffle(d)
print(d)

# 예제16 (무작위 선택)
c = random.choice(d)
print(c)

# webbrower : 본인 os의 웹 브라우저 실행
import webbrowser
webbrowser.open("http://google.com")
webbrowser.open_new("http://google.com") # 새 탭을 열어서 사용

