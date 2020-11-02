# What’s the password.md
The picture says that the password is "sudo", let's try steghide with passphrase sudo
```
$steghide extract -sf sudo.jpg
Enter passphrase: sudo
wrote extracted data to "steganopayload457819.txt".
$cat steganopayload457819.txt
CYCTF{U$3_sud0_t0_achi3v3_y0ur_dr3@m$!}
```
