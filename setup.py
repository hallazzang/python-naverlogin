"""
==========
naverlogin
==========

naverlogin is a tiny module for Naver(Korean portal site) login.

Easy to use
-----------

``NaverSession``, the only class which naverlogin exposes
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
"""

from setuptools import setup

setup(
    name='naverlogin',
    version='1.0.1',
    url='https://github.com/hallazzang/python-naverlogin',
    license='MIT',
    author='hallazzang',
    author_email='hallazzang@gmail.com',
    description='A tiny module for Naver login',
    long_description=__doc__,
    py_modules=['naverlogin'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'rsa>=3.4.2',
        'requests>=2.18.3',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)