#!/usr/bin/python3

"""The base command."""
import http.client
import logging

from ..lib.tabulate import tabulate


class Base(object):
    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs
        self.conn = None

    def run(self):
        self.options
        raise NotImplementedError('You must implement the run() method yourself!')

    def _open(self):
        if self.conn:
            return
        self.conn = http.client.HTTPConnection(self.options.get('--server'), self.options.get('--port'))

    def _print(self, keys, result):
        table = []
        table.append(keys)
        if isinstance(result, list):
            for item in result:
                self.__parse(item, keys, table)
        else:
            self.__parse(result, keys, table)

        tabulate(table, headers="firstrow")
        print(tabulate(table))

    @staticmethod
    def __parse(item, keys, table):
        innertable = []
        table.append(innertable)
        for key in keys:
            key = key.strip()
            if "." in key:
                subkeys = key.split('.')
                inner_data = item.get(subkeys[0])
                items = []
                if inner_data:
                    if isinstance(inner_data, list):
                        for l in inner_data:
                            items.append(l.get(subkeys[1]))
                    else:
                        items.append(str(inner_data.get(subkeys[1])))
                innertable.append(' '.join(items))
            else:
                res = str(item.get(key))
                # if key == "id":
                #     res = res[:12]
                innertable.append(res)

    def _send(self, path, method='GET', data=None):
        try:
            from base64 import b64encode
            self._open()

            userAndPass = self.options.get('--login') + ':' + self.options.get('--password')
            bAuth = b64encode(str.encode(userAndPass)).decode("ascii")
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Basic %s' % bAuth
            }

            self.conn.request(method, path, data, headers=headers)
        except Exception as ex:
            self.conn.close()
            self.conn = None
            logging.error("Can not connect to dm %s due to error: %s", self.options.get('--server'), ex)
            raise
        resp = self.conn.getresponse()
        if resp.status > 300:
            raise Exception("Invalid response: {} {} from {}"
                            .format(resp.status, resp.reason, self.options.get('--server')))
        return resp.read().decode('utf8')
