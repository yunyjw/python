'''
package python;

import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

public class test {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		
		 String config  = "<?xml version='1.0'?>";
				config += "<WLANProfile xmlns='http://www.microsoft.com/networking/WLAN/profile/v1'>";
				config += "	<name>KT_GiGA_5G_Wave2_D72F</name>";
				config += "	<SSIDConfig>";
				config += "		<SSID>";
				config += "			<hex>4B545F476947415F35475F57617665325F44373246</hex>";
				config += "			<name>KT_GiGA_5G_Wave2_D72F</name>";
				config += "		</SSID>";
				config += "	</SSIDConfig>";
				config += "	<connectionType>ESS</connectionType>";
				config += "	<connectionMode>auto</connectionMode>";
				config += "	<MSM>";
				config += "		<security>";
				config += "			<authEncryption>";
				config += "				<authentication>WPA2PSK</authentication>";
				config += "				<encryption>AES</encryption>";
				config += "				<useOneX>false</useOneX>";
				config += "			</authEncryption>";
				config += "			<sharedKey>";
				config += "				<keyType>passPhrase</keyType>";
				config += "				<protected>false</protected>";
				config += "				<keyMaterial>cfdabfk652</keyMaterial>";
				config += "			</sharedKey>";
				config += "		</security>";
				config += "	</MSM>";
				config += "	<MacRandomization xmlns='http://www.microsoft.com/networking/WLAN/profile/v3'>";
				config += "		<enableRandomization>false</enableRandomization>";
				config += "		<randomizationSeed>2390514083</randomizationSeed>";
				config += "	</MacRandomization>";
				config += "</WLANProfile>";
//				 "C:\\WINDOWS\\system32\\cmd.exe"; 
		
				
		// 폴더 만드는 부분 		
		String path = "C:\\WIFI";		
		File test = new File(path);
		
		// 해당 경로에 폴더가 없을때 생성
		if(test.exists() == false) {
			test.mkdir();
		}

		
		int num = 1;
		
		if(num == 1) {
			// XML 파일 만드는 부분
			FileOutputStream xmlFile = new FileOutputStream("C:\\WIFI\\Wi-Fi-TEST.xml");
			
			BufferedOutputStream buffer1 = new BufferedOutputStream(xmlFile);
			
			buffer1.write(config.getBytes());
			
			buffer1.close();
			
			
			// bat 파일 만드는 부분
			FileOutputStream batFile = new FileOutputStream("C:\\WIFI\\Wi-Fi-BAT-TEST.bat");
			
			BufferedOutputStream buffer2 = new BufferedOutputStream(batFile);
			
			buffer2.write(config.getBytes());
			
			buffer2.close();
			
		} else if(num == 2) {
			// XML 파일 만드는 부분
			FileOutputStream xmlFile = new FileOutputStream("C:\\WIFI\\Wi-Fi-TEST.xml");
			
			BufferedOutputStream buffer1 = new BufferedOutputStream(xmlFile);
			
			buffer1.write(config.getBytes());
			
			buffer1.close();
			
			
			// bat 파일 만드는 부분
			FileOutputStream batFile = new FileOutputStream("C:\\WIFI\\Wi-Fi-BAT-TEST.bat");
			
			BufferedOutputStream buffer2 = new BufferedOutputStream(batFile);
			
			buffer2.write(config.getBytes());
			
			buffer2.close();
		} else {
			System.out.println("ㅅㄱ");
		}
		
		
		// https://gomming.tistory.com/6 
		
		
	}

}
'''