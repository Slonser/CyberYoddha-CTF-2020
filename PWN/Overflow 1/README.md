# Overflow 1
A non-secure function gets(it does not check the length of user input) is used for user input
```
  char str[] = "AAAA";
  char buf[16];
  gets(buf);
  if (!(str[0] == 'A' && str[1] == 'A' && str[2] == 'A' && str[3] == 'A')){
    system("/bin/sh");
  }
```
It is enough to overwrite 1 byte of str located directly under buf,that is, enter any 17 characters.