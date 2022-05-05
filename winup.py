# 숨겨진 ssid 자동 설정 exe 파일
# 작업 순서 
'''
1. daeduck_office xml 파일을 사용자 C:\Wi-Fi 폴더를 만들어서 추가 
2. daeduck_office ssid 프로필 추가
3. daeduck_office ssid 접속
4. daeduck_office ssid 자동 연결
'''
# daeduck_office xml 파일 내용
from cmd import Cmd
import cmd
import os
from posixpath import join
import sys
from tkinter import N, OFF
from typing_extensions import ParamSpec
#import win32com.shell.shell as shell
from pathlib import Path
from time import sleep
import win32comext.shell.shell as shell
import subprocess




# C:\Temp 라는 경로가 있는지를 검사하고 없으면 생성 할 수 있다.
# parents: True는 상위 path가 없는 경우 새로 생성함, Flase는 상위 path가 없으면 FileNotFountError를 발생함

Path('C:\\Temp').mkdir(parents=True, exist_ok=True)

# c:\temp\daeduck_office.xml 파일 생성 후 아래 내용 출력
f = open("C:\\Temp\\winup.bat", 'w')
f.write('reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate\AU" /v AUOptions /t REG_DWORD /d 4 /f \n')

f.write('reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate\AU" /v NoAutoRebootWithLoggedOnUsers /t REG_DWORD /d 0 /f \n')

f.write('reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate\AU" /v NoAutoUpdate /t REG_DWORD /d 0 /f \n')

f.write('reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate\AU" /v ScheduledInstallDay /t REG_DWORD /d 0 /f \n')

f.write('reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate\AU" /v ScheduledInstallTime /t REG_DWORD /d 12 /f \n')

f.close()
os.system('"C:\\Temp\\winup.bat"')

'''
# 관리자 권한 상승 요청 함수
def uac_require():
    asadmin ='asadmin'
    try:
        if sys.argv[-1] != asadmin:
            script = os.path.abspath(sys.argv[0])
            Params = ' '.join([script] + sys.argv[1:] + [asadmin])
            shell.ShellExecuteEx(IpVerb='runas', IpFile=sys.executable, IpParameter=Params)
            os.system('reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate\AU" /v AUOptions /t REG_DWORD /d 4 /f')
            sleep(3)
            os.system('reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate\AU" /v NoAutoRebootWithLoggedOnUsers /t REG_DWORD /d 0 /f')
            os.system('reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate\AU" /v NoAutoUpdate /t REG_DWORD /d 0 /f')
            os.system('reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate\AU" /v ScheduledInstallDay /t REG_DWORD /d 0 /f')
            os.system('reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate\AU" /v ScheduledInstallTime /t REG_DWORD /d 12 /f')

            sys.exit()
        return True
    except:
        return False
uac_require()
'''

'''
# pyinstaller  --uac-admin  sample.py / [주의] -F / --onefile 옵션과 함께 사용 안됨
# ssid 프로파일 추출 명령어 ( XML 파일을 사용자 PC에 저장시키면 이 작업은 굳이 안해도 됨)
# os.system('netsh wlan export profile name=daeduck_office key=clear folder=c:\\Wi-Fi')
# 신규 프로파일 추가 명령어
os.system('reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate\AU" /v AUOptions /t REG_DWORD /d 4 /f')
# 3초간 쉬었다가 명령어 실행
# 프로파일 이용하여 ssid 접속 명령어 ( Wi-Fi )
sleep(3)
os.system('reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate\AU" /v NoAutoRebootWithLoggedOnUsers /t REG_DWORD /d 0 /f')
# 추가 한 ssid에 자동 연결 시키는 명령어
os.system('reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate\AU" /v NoAutoUpdate /t REG_DWORD /d 0 /f')
os.system('reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate\AU" /v ScheduledInstallDay /t REG_DWORD /d 0 /f')
os.system('reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate\AU" /v ScheduledInstallTime /t REG_DWORD /d 12 /f')
'''