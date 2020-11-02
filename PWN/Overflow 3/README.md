# Overflow 3
We have a main function that reads user data. Again, the vulnerable "gets" function.
```
	long vuln = 0;
        char buf[16];

	gets(buf);

	if (vuln == 0xd3adb33f){
		system("/bin/sh");
	}
```
Just enter any 16 characters and 0xd3adb33f in little endian and get shell.  
### CYCTF{wh0@_y0u_jump3d_t0_th3_funct!0n}
