# 숨겨진 ssid 자동 설정 exe 파일
# 작업 순서 
'''
1. daeduck_office xml 파일을 사용자 C:\Wi-Fi 폴더를 만들어서 추가 
2. daeduck_office ssid 프로필 추가
3. daeduck_office ssid 접속
4. daeduck_office ssid 자동 연결
'''
# daeduck_office xml 파일 내용
import os
from posixpath import join
import sys
from typing_extensions import ParamSpec
import win32com.shell.shell as shell
from pathlib import Path
from time import sleep


# C:\Temp 라는 경로가 있는지를 검사하고 없으면 생성 할 수 있다.
# parents: True는 상위 path가 없는 경우 새로 생성함, Flase는 상위 path가 없으면 FileNotFountError를 발생함
Path('C:\\Temp').mkdir(parents=True, exist_ok=True)


# c:\temp\daeduck_office.xml 파일 생성 후 아래 내용 출력
f = open("C:\\Temp\\Wi-Fi-daeduck_office.xml", 'w')
ssid_1 = '<?xml version="1.0"?>'
ssid_2 = '  <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">'
ssid_3 = '  <name>daeduck_office</name>'
ssid_4 =  '	<SSIDConfig>'
ssid_5 =  '		<SSID>'
# [중요] ssid 별로 hex값이 다르기 때문에 수동으로 wifi 잡은 다음 파일 export 하여 값 확인 필요
ssid_6 =  '			<hex>6461656475636B5F6F6666696365</hex>'
ssid_7 =  '			<name>daeduck_office</name>'
ssid_8 =  '		</SSID>'
ssid_9 =  '		<nonBroadcast>true</nonBroadcast>'
ssid_10 = '	</SSIDConfig>'
ssid_11 = '	<connectionType>ESS</connectionType>'
ssid_12 = '	<connectionMode>auto</connectionMode>'
ssid_13 = '	<MSM>'
ssid_14 = '		<security>'
ssid_15 = '			<authEncryption>'
ssid_16 = '				<authentication>WPA2PSK</authentication>'
ssid_17 = '				<encryption>AES</encryption>'
ssid_18 = '				<useOneX>false</useOneX>'
ssid_19 = '			</authEncryption>'
ssid_20 = '			<sharedKey>'
ssid_21 = '				<keyType>passPhrase</keyType>'
ssid_22 = '				<protected>false</protected>'
ssid_23 = '				<keyMaterial>daeduckwireless12345543210</keyMaterial>'
ssid_24 = '			</sharedKey>'
ssid_25 = '		</security>'
ssid_26 = '	</MSM>'
ssid_27 = ' </WLANProfile>'
f.write(ssid_1)
f.write('\n')
f.write(ssid_2)
f.write('\n')
f.write(ssid_3)
f.write('\n')
f.write(ssid_4)
f.write('\n')
f.write(ssid_5)
f.write('\n')
f.write(ssid_6)
f.write('\n')
f.write(ssid_7)
f.write('\n')
f.write(ssid_8)
f.write('\n')
f.write(ssid_9)
f.write('\n')
f.write(ssid_10)
f.write('\n')
f.write(ssid_11)
f.write('\n')
f.write(ssid_12)
f.write('\n')
f.write(ssid_13)
f.write('\n')
f.write(ssid_14)
f.write('\n')
f.write(ssid_15)
f.write('\n')
f.write(ssid_16)
f.write('\n')
f.write(ssid_17)
f.write('\n')
f.write(ssid_18)
f.write('\n')
f.write(ssid_19)
f.write('\n')
f.write(ssid_20)
f.write('\n')
f.write(ssid_21)
f.write('\n')
f.write(ssid_22)
f.write('\n')
f.write(ssid_23)
f.write('\n')
f.write(ssid_24)
f.write('\n')
f.write(ssid_25)
f.write('\n')
f.write(ssid_26)
f.write('\n')
f.write(ssid_27)
f.write('\n')
f.close()

# 관리자 권한 상승 요청 함수
def uac_require():
    asadmin ='asadmin'
    try:
        if sys.argv[-1] != asadmin:
            script = os.path.abspath(sys.argv[0])
            Params = 'join([script] + sys.argv[1:] + [asadmin])'
            shell.ShellExecuteEx(IpVerb='runas', IpFile=sys.executable, IpParameter=Params)
            sys.exit()
        return True
    except:
        return False

'''
# __name__ 이라는 변수의 값이 __main__이라면 아래의 코드를 실행하라 ( 오류 발생 )
if __name__=='__main__'
    import win32com.shell.shell as shell
    import os,sys

    if uac_require():           # 관리자 권한 요청 함수 실행
        print("continue")       # 권한 상승 시 True를 리턴 받아서 다음 작업 수행
    else:                       # 관리자 권한으로 실행 안되면 False 받아 else 문 수행
        print("error message")  # else문에 별도의 메시지를 넣거나 종료 등을 수행
'''

# pyinstaller  --uac-admin  sample.py / [주의] -F / --onefile 옵션과 함께 사용 안됨
# ssid 프로파일 추출 명령어 ( XML 파일을 사용자 PC에 저장시키면 이 작업은 굳이 안해도 됨)
# os.system('netsh wlan export profile name=daeduck_office key=clear folder=c:\\Wi-Fi')
# 신규 프로파일 추가 명령어
os.system('netsh wlan add profile filename="C:\\Temp\\Wi-Fi-daeduck_office.xml" Interface="Wi-Fi" user=current')
# 3초간 쉬었다가 명령어 실행
# 프로파일 이용하여 ssid 접속 명령어 ( Wi-Fi )
sleep(3)
os.system('netsh wlan connect ssid=daeduck_office name=daeduck_office interface=Wi-Fi')
# 추가 한 ssid에 자동 연결 시키는 명령어
os.system('netsh wlan set profileparameter name=daeduck_office connectionmode=auto')
