import os
from pathlib import Path

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