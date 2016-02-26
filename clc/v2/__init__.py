import json
import requests

class AuthError(Exception):
    pass


class ClientV2:
    def __init__(self, config, **kw):
        self.config = config
        self.auth = None
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.headers["Accept"] = "application/json"
        self.headers["User-Agent"] = "py-clc-sdk"
        for k,v in kw.get('headers', []):
            self.headers[k] = v

    def authenticate(self):
        url = "/".join([self.config.uri_v2, "v2/authentication/login"])
        data = dict(username=self.config.username,
                    password=self.config.password)
        resp = requests.post(url, data=json.dumps(data), headers=self.headers)
        # error check resp
        if resp.status_code != 200:
            raise AuthError, resp
        self.auth = resp.json()
        self.headers['Authorization'] = self.auth['bearerToken']
        return True

    def request(self, path, verb, data=None, raw=False):
        url = "/".join([self.config.uri_v2, path])
        if data and not raw:
            # json-encode all arguments
            data = json.dumps(data)
        return requests.Request(method, url, data=data, headers=self.headers)
