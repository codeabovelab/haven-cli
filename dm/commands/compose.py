from json import dumps

from .base import Base


class Compose(Base):
    def run(self):
        # /clusters/{cluster}/compose
        try:
            from base64 import b64encode
            self._open()

            userAndPass = self.options.get('--login') + ':' + self.options.get('--password')
            bAuth = b64encode(str.encode(userAndPass)).decode("ascii")
            headers = {
                "Content−type": "application/octet−stream",
                'Authorization': 'Basic %s' % bAuth
            }
            # self.conn.request(method, path, data, headers=headers)
            self.conn.request("POST", "/clusters/" + self.options.get('--cluster') + "/compose", open(self.options.get('--file'), "rb"), headers)
        except Exception as ex:
            self.conn.close()
            self.conn = None
            logging.error("Can not connect to dm %s due to error: %s", self.options.get('--server'), ex)
            raise
        resp = self.conn.getresponse()
        if resp.status > 300:
            raise Exception("Invalid response: {} {} from {}"
                            .format(resp.status, resp.reason, self.options.get('--server')))
        result = json.loads(resp.read().decode('utf8'))
        keys = ['id', 'name', 'node', 'cluster', 'image', 'ports', 'status']
        self._print(keys, result)