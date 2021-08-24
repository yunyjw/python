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
'''
import xml.etree.ElementTree as ET

xml = <?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
	<name>daeduck_office</name>
	<SSIDConfig>
		<SSID>
			<hex>6461656475636B5F414756</hex>
			<name>daeduck_office</name>
		</SSID>
		<nonBroadcast>true</nonBroadcast>
	</SSIDConfig>
	<connectionType>ESS</connectionType>
	<connectionMode>manual</connectionMode>
	<MSM>
		<security>
			<authEncryption>
				<authentication>WPA2PSK</authentication>
				<encryption>AES</encryption>
				<useOneX>false</useOneX>
			</authEncryption>
			<sharedKey>
				<keyType>passPhrase</keyType>
				<protected>false</protected>
				<keyMaterial>daeduckwireless12345543210</keyMaterial>
			</sharedKey>
		</security>
	</MSM>
</WLANProfile>
'''

# ssid 프로파일 추출 명령어 ( XML 파일을 사용자 PC에 저장시키면 이 작업은 굳이 안해도 됨)
os.system('netsh wlan export profile name=daeduck_office key=clear folder=c:\Wi-Fi')
# 신규 프로파일 추가 명령어
os.system('netsh wlan add profile filename="C:\Wi-Fi\Wi-Fi-daeduck_office.xml" Interface="Wi-Fi" user=current')
# 프로파일 이용하여 ssid 접속 명령어 ( Wi-Fi )
os.system('netsh wlan connect ssid=daeduck_AGV name=daeduck_office interface=Wi-Fi')
# 추가 한 ssid에 자동 연결 시키는 명령어
os.system('netsh wlan set profileparameter name=daeduck_office connectionmode=auto')

