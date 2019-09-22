import os,platform

"Set Color"
if platform.system() == "linux" or platform.system() == "linux2":
        W = ""
        G = ""
        R = ""
        N = ""
        Y = ""
else:
        W = "\033[37m"
        G = "\033[32m"
        R = "\033[31m"
        N = "\033[0m"
        Y = "\033[33m"
try:
	import os,sys,time
except Exception as E:
	print (R+"ERROR: "+W+str(E))

def show_commands():
	print ("""command:
   set text [text] => to set text
   set hash [type] => set type hash
   run             => to run hash crypt framework
   help or ? or -h => to show commands or help programs
   about           => to about this tool

type:
   md4 
   md5
   mysql323
   sha1
   whirlpool
   mssql2005""")

