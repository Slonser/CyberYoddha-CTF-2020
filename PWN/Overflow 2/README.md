# Overflow 2
We have the vuln function and the run_shell function.the first one contains the vulnerable gets function, thanks to which we can rewrite the return address and go to the second function
```
void vuln()
{
  char buf[16]; 
  gets(buf);
}
void run_shell()
{
  system("/bin/sh");
}
```
You can check the stack view of this function
```
#-00000018 buf             db 16 dup(?)
#-00000008                 db ? ; undefined
#-00000007                 db ? ; undefined ->  this is 32 bit offset
#-00000006                 db ? ; undefined
#-00000005                 db ? ; undefined
#-00000004 var_4           dd ?
#+00000000  s              db 4 dup(?) -> this canary
#+00000004  r              db 4 dup(?) -> this return address
#+00000008
#+00000008 ; end of stack variables
```
We need to enter 28 bytes to get to the return address.After that, rewrite the return address to `0x08049172` (This is the address of the run_shell function).  
### CYCTF{0v3rfl0w!ng_v@ri@bl3$_i$_3z}
