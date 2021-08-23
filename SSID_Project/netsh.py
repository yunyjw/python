'''
netsh wlan export profile name=daeduck_AGV key=clear folder=c:\Wi-Fi
netsh wlan add profile filename="C:\Wi-Fi\Wi-Fi-daeduck_office.xml" Interface="Wi-Fi" user=current
netsh wlan connect ssid=daeduck_office name=daeduck_office interface=Wi-Fi
netsh wlan set profileparameter name=daeduck_office connectionmode=auto
'''
