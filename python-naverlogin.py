# python-naverlogin.py
# https://github.com/HallaZzang/python-naverlogin.git

import requests
import re
import rsa
from binascii import hexlify

class NaverSession(requests.Session):
    def login(self, user_id, user_pw, do_finalize=True):
        keys = self._get_keys()

        public_key = rsa.PublicKey(keys['evalue'], keys['nvalue'])
        raw_data = chr(len(keys['sessionkey'])) + keys['sessionkey'] + \
                   chr(len(user_id)) + user_id + chr(len(user_pw)) + user_pw
        enc_data = rsa.encrypt(raw_data, public_key)

        login_url = 'https://nid.naver.com/nidlogin.login'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://www.naver.com/',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        params = {
            'enctp': 1,
            'encpw': hexlify(enc_data),
            'encnm': keys['keyname'],
            'svctype': 0,
            'url': 'http://www.naver.com/',
            'enc_url': 'http%3A%2F%2Fwww.naver.com%2F',
            'postDataKey': '',
            'nvlong': '',
            'saveID': '',
            'smart_level': 'undefined',
            'id': '',
            'pw': ''
        }
        resp = self.post(login_url, params, headers=headers).content

        if 'https://nid.naver.com/login/sso/finalize.nhn' in resp:
            if do_finalize:
                finalize_url_pattern = r'location\.replace\("(.+?)"\);'
                finalize_url = re.findall(finalize_url_pattern, resp)[0]

                headers['Referer'] = 'https://nid.naver.com/nidlogin.login'
                del headers['Content-Type']

                resp = self.get(finalize_url, headers=headers).content

                return 'location.replace("http://www.naver.com/")' in resp
            return True
        else:
            return False

    def logout(self):
        logout_url = 'http://nid.naver.com/nidlogin.logout'
        self.get(logout_url)

    def _get_keys(self):
        fetch_url = 'http://static.nid.naver.com/loginv3/js/keys_js.nhn'
        content = self.get(fetch_url).content

        key_pattern = r'(sessionkey|keyname|evalue|nvalue) = \'(.+)\';'
        keys = dict(re.findall(key_pattern, content))
        keys['nvalue'] = int(keys['nvalue'], 16)
        keys['evalue'] = int(keys['evalue'], 16)

        return keys