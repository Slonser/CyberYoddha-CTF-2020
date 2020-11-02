#Something Sw33t
If we check the Cookie, we will find a base64 string there,and if we try to decode it, we will get a string that does not carry a semantic load.Because it's [Flask cookies](https://pypi.org/project/flask-cookie-decode/)
Let's decrypt
```
{' b': 'bm90X2V4aXN0YW50'}, 'name': {' b': 'Cynthia Astley'}}, {'description': {' b': 'nicee='}, 'flag': {' b': 'YmFzZTY0X2lzX3N1cHJlbWU='}, 'name': {' b': 'Horace Astley'}}, {'description': {' b': 'human'}, 'flag': {' b': 'flag=flag'}, 'name': {'
b': ''}}, {'description': {' b': 'the man'}, 'flag': {' b': 'Q1lDVEZ7MGtfMV9zZWVfeW91X21heWJlX3lvdV9hcmVfc21hcnR9'}, 'name': {' b': 'Rick Astley'}}, {'description': {' b': 'yeedeedeedeeeeee'}, 'flag': {' b': 'dHJ5X2FnYWlu'}, 'name': {' b': 'Lene Bausager'}}, {'description': {' b': 'uhmm'}, 'flag': {' b': 'bjBwZWVlZQ=='}, 'name': {' b': 'Jayne Marsh'}}, {'description': {' b': 'hihi'}, 'flag': {' b': 'bjBfYjB0c19oM3Iz'}, 'name': {' b': 'Emilie Astley'}}]}}, expiration='2020-11-16T23:40:39')
```
We see a lot of base64 strings let's decipher each one and look for the flag
`Q1lDVEZ7MGtfMV9zZWVfeW91X21heWJlX3lvdV9hcmVfc21hcnR9 = CYCTF{0k_1_see_you_maybe_you_are_smart}`
###CYCTF{0k_1_see_you_maybe_you_are_smart}