=================
python-naverlogin
=================

python-naverlogin is a tiny module for Naver(Korean portal site) login.

Easy to use
-----------

``NaverSession``, the only class which python-naverlogin exposes
inherits ``requests.Session`` and adds two methods(``login``, ``logout``).
It's obvious what these methods would do.

.. code:: python

    import re

    from naverlogin import NaverSession

    naver = NaverSession()
    if naver.login('YOUR_ID', 'YOUR_PASSWORD'):
        # Fetch user's information.
        r = naver.get('https://nid.naver.com/user2/help/myInfo.nhn?lang=ko_KR')
        name = re.search(r'<dd class="nic_desc">(.+?)</dd>', r.text).group(1)

        print(u'Hello, {}!'.format(name))

        # Logout immediately to prevent dirty activity logs from being left.
        naver.logout()
    else:
        print(u'Login failed - check ID and password.')

Less dependencies
-----------------

It does not require any javascript emulators, while others might use
Selenium, Ghost.py, or SpiderMonkey.
It only depends on ``rsa`` and ``requests`` modules.

Installation
------------

.. code:: bash

    $ pip install naverlogin