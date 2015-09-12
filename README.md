# python-naverlogin
Tiny module that can help who wants to use naver login in his/her application

Features
--------
- It doesn't need any JavaScript emulator to use `rsa.js` cause it was written in pure Python.
- Easy to use; the `NaverSession` class just overrides `requests.Session`. The only difference is it has `login` and `logout` method(...and `_get_keys` method, too).

Example usage
-------------
```python
from naverlogin import NaverSession

nsession = NaverSession()
if nsession.login('blahblah', 'foofoo'):
    print 'login finished.'
    
    # do your job
    
    nsession.logout()
else:
    print 'login failed! check id and password.')
```

Notes
-----
- It requires `requests` module.
- It was written in `Python 2.7`.
