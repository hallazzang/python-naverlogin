# python-naverlogin
Tiny module that can help who wants to use naver login in his/her application

Features
--------
- It doesn't need any JavaScript emulator to run `rsa.js`.
- Easy to use: `NaverSession` class just overrides `requests.Session`. The only difference between those two classes is `NaverSession` has additional methods, `login` and `logout`(...and `_get_keys` method, too).

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
- It was developed in `Python 2.7`.
