# _*_ coding=UTF-8 _*_
import os,platform

"""
__Codded__ : BL4CK DR460N
__Team__   : WOLL CYBER TEAM & BL4CK C0D3R CRUSH
__Version__: 1 (low version)

Copyright (c) @BL4CK_DR460N

Bacotan BL4CK DR460N

Hargai lah para noob
Hargai lah karya orang lain
Hargai lah karya BL4CK DR460N
Jangan banyak bacot
Jangan recode ajg
Langsung pake aja apa susah nya
W udh susah payah membuat tool ini
Jadi Lu Jangan Recode Yaa ^_^

Terima Kasih Sudah Dengar Bacotaan Q Yang Gk Di Fahamin Orang²
"""



"Set Color"
if platform.system() == "linux" or platform.system() == "linux2":
	W = ""
	G = ""
	R = ""
	N = ""
	Y = ""
else:
	W = "\033[37;1m"
        G = "\033[32;1m"
        R = "\033[31;1m"
        N = "\033[0m"
        Y = "\033[33;1m"
try:
	import sys,time,hashlib,help,passlib
except Exception as E:
	print (R+"ERROR: "+W+str(E))
	sys.exit()
def exit():
	print (W+"[!] Thanks To Using This Tool ^_^")
	sys.exit()

def generate():
	if not os.path.exists('.text'):
		os.mkdir(".text")
	else:
		pass
	if not os.path.exists('result'):
		os.mkdir("result")
	else:
		pass
	try:
		open(".text/.text.txt","r").read()
		os.system("rm -rf .text/.text.txt")
	except IOError:
		pass
class hash:
	def md5_enc(self, text):
		md5 = hashlib.md5(text.encode("utf-8")).hexdigest()
		return md5
	def sha1_enc(self, text):
		sha1 = hashlib.sha1(text.encode("utf-8")).hexdigest()
		return sha1
	def md4_enc(self, text):
		m = hashlib.new("md4")
		m.update(text)
		md4 = m.hexdigest()
		return md4
	def sql1(self,text):
		from passlib.hash import mysql323
		sql = mysql323.encrypt(text)
		return sql
	def whirlpool_enc(self, text):
		enc = hashlib.new("whirlpool")
		enc.update(text.encode("utf-8"))
		hasil = enc.hexdigest()
		return hasil
	def mssql2005(self,text):
		from passlib.hash import mssql2005 as m25
		mssql2005 = m25.encrypt(text)
		return mssql2005

class banner:
	def logo(self):
		os.system('clear')
		print ("""{}
 _  _   _   ___ _  _      ___ _____   _____ _____
| || | /_\ / __| || |___ / __| _ \ \ / / _ \_   _|{}
| __ |/ _ \\__ \  __ |___| (__|   /\ V /|  _/ | |
|_||_/_/ \_\___/_||_|    \___|_|_\ |_| |_|   |_|{}
  [{}DEVELOPER{}] {}BL4CK DR460N{}
  [{}NAME TOOL{}] {}HASH CRYPT Framework{}
  [{}   TEAM  {}] {}WOLL CYBER TEAM & BL4CK C0D3R CRUSH{}
  [{} VERSION {}] 1 {}(low scurity){}
===================================================={}""").format(R,W,Y,G,Y,W,Y,G,Y,W,Y,G,Y,W,Y,G,Y,R,Y,N)
class main_menu:
	def menu(self):
		ban = banner()
		ban.logo()
		self.shell()
	def shell(self):
		global text, type
		while True:
			try:
				p = raw_input(W+"["+Y+"?"+W+"] "+R+"HCF> "+G)
				pil = p.split()
				if p in [""," ","  "]:
					print (W+"["+R+"-"+W+"] "+R+"please input commands")
				elif p in ["help","-h","?"]:
					help.show_commands()
				elif p in ["exit","quit"]:
					exit()
				elif pil[0] == "set":
					if pil[1] == "text":
						try:
							if not pil[2]:
								print (W+"["+R+"-"+W+"] "+R+"please input text")
							if pil[2] == " ":
								print (W+"["+R+"-"+W+"] "+R+"please enter 1 word")
							else:
								open(".text/.text.txt","w").write(pil[2])
						except:
							print (W+"["+R+"-"+W+"] "+R+"unknown errors")
					elif pil[1] == "hash":
						try:
							if not pil[2]:
								print (W+"["+R+"-"+W+"] "+W+"please input type")
							else:
								type = pil[2]
						except:
							print (W+"["+R+"-"+W+"] "+R+"unknown errors")
					else:
                                                print (W+"["+R+"-"+W+"] "+R+"unknown commands "+W+"'"+pil[1]+"'")
				elif p == "run":
					try:
						text = open(".text/.text.txt","r").read()
					except IOError:
						print (W+"["+R+"-"+W+"] "+R+"please set text")
					else:
						if type == "md5":
							md5 = hash().md5_enc(text)
							print (W+"["+G+"+"+W+"] "+Y+"MD5 : "+G+str(md5))
							open("result/md5.txt","a").write(text+"|"+md5)
						elif type == "sha1":
							sha1 = hash().sha1_enc(text)
							print (W+"["+G+"+"+W+"] "+Y+"SHA1 : "+G+str(sha1))
							open("result/sha1.txt","a").write(text+"|"+sha1)
						elif type == "whirlpool":
							whirlpool = hash().whirlpool_enc(text)
							print (W+"["+G+"+"+W+"] "+Y+"WHIRLPOOl : "+G+str(whirlpool))
							open("result/wirlpool.txt","a").write(text+"|"+wirlpool)
						elif type == "md4":
							md4 = hash().md4_enc(text)
							print (W+"["+G+"+"+W+"] "+Y+"MD4 : "+G+str(md4))
							open("result/md4.txt","a").write(text+"|"+md4)
						elif type == "mysql323":
							sql = hash().sql1(text)
							print (W+"["+G+"+"+W+"] "+Y+"MYSQL323 : "+G+str(sql))
							open("result/mysql323.txt","a").write(text+"|"+sql)
						elif type == "mssql2005":
							sql = hash().mssql2005(text)
							print (W+"["+G+"+"+W+"] "+Y+"MSSQL2005 : "+G+str(sql))
							open("result/mssql2005.txt","a").write(text+"|"+sql)
						else:
							print (W+"["+R+"-"+W+"]"+W+" unknown type hash")
						
				else:
					print (W+"["+R+"-"+W+"]"+R+" Unknown commands "+W+"'"+pil[0]+"'")
			except EOFError:
				print (R+"\nERROR: "+W+"please 'exit' to exit programs")
			except KeyboardInterrupt:
				print (R+"\nERROR: "+W+"please 'exit' to exit programs")

if __name__ == '__main__':
	generate()
	run = main_menu()
	run.menu()
