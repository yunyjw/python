# 숨겨진 ssid 자동 설정 exe 파일
# 작업 순서 
'''
1. daeduck_office xml 파일을 사용자 C:\Wi-Fi 폴더를 만들어서 추가 
2. daeduck_office ssid 프로필 추가
3. daeduck_office ssid 접속
4. daeduck_office ssid 자동 연결
'''

import os
# daeduck_office xml 파일 내용

# c:\temp\daeduck_office.xml 파일 생성 후 아래 내용 출력
f = open("C:\\temp\\daeduck_office.xml", 'w')
ssid_1 = 'xml = <?xml version="1.0"?>'
ssid_2 = '  <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">'
ssid_3 = '  <name>daeduck_office</name>'
ssid_4 =  '	<SSIDConfig>'
ssid_5 =  '		<SSID>'
ssid_6 =  '			<hex>6461656475636B5F414756</hex>'
ssid_7 =  '			<name>daeduck_office</name>'
ssid_8 =  '		</SSID>'
ssid_9 =  '		<nonBroadcast>true</nonBroadcast>'
ssid_10 = '	</SSIDConfig>'
ssid_11 = '	<connectionType>ESS</connectionType>'
ssid_12 = '	<connectionMode>manual</connectionMode>'
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

# ssid 프로파일 추출 명령어 ( XML 파일을 사용자 PC에 저장시키면 이 작업은 굳이 안해도 됨)
# os.system('netsh wlan export profile name=daeduck_office key=clear folder=c:\\Wi-Fi')
# 신규 프로파일 추가 명령어
os.system('netsh wlan add profile filename="C:\\temp\\daeduck_office.xml" Interface="Wi-Fi" user=current')
# 프로파일 이용하여 ssid 접속 명령어 ( Wi-Fi )
os.system('netsh wlan connect ssid=daeduck_office name=daeduck_office interface=Wi-Fi')
# 추가 한 ssid에 자동 연결 시키는 명령어
os.system('netsh wlan set profileparameter name=daeduck_office connectionmode=auto')

