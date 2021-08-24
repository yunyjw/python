'''
netsh wlan export profile name=daeduck_AGV key=clear folder=c:\Wi-Fi
netsh wlan add profile filename="C:\Wi-Fi\Wi-Fi-daeduck_office.xml" Interface="Wi-Fi" user=current
netsh wlan connect ssid=daeduck_office name=daeduck_office interface=Wi-Fi
netsh wlan set profileparameter name=daeduck_office connectionmode=auto
'''

import os
# import subprocess # subprocess는 파이썬에서 쉘 명령을 실행할 수 있게 해주는 라이브러리

# ssid 프로파일 추출 명령어
os.system('netsh wlan export profile name=daeduck_AGV key=clear folder=c:\Wi-Fi')
# 신규 프로파일 추가 명령어
os.system('netsh wlan add profile filename="C:\Wi-Fi\Wi-Fi-daeduck_AGV.xml" Interface="Wi-Fi" user=current')
# 프로파일 이용하여 ssid 접속 명령어 ( Wi-Fi )
os.system('netsh wlan connect ssid=daeduck_AGV name=daeduck_AGV interface=Wi-Fi')
# 추가 한 ssid에 자동 연결 시키는 명령어
os.system('netsh wlan set profileparameter name=daeduck_AGV connectionmode=auto')
