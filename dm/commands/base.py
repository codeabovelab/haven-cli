#!/usr/bin/python3

"""The base command."""
import http.client
import logging


class Base(object):
    """A base command."""

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs
        self.conn = None

    def run(self):
        self.options
        raise NotImplementedError('You must implement the run() method yourself!')

    def __open(self):
        if self.conn:
            return
        self.conn = http.client.HTTPConnection(self.options.get('--server'), self.options.get('--port'))

    def _send(self, path, method='GET', data=None):
        self.last_req_info = {'method': method, 'path': path, 'data': data}
        try:
            self.__open()
            self.conn.request(method, path)
        except:
            self.conn.close()
            self.conn = None
            logging.error("Can not connect to dm %s due to error: %s", self.gather_error_info(), sys.exc_info()[1])
            raise
        resp = self.conn.getresponse()
        if resp.status != '200':
            raise Exception("Invalid response: {} {} from {}"
                            .format(resp.status, resp.reason, self.options.get('--server')))
        return json.loads(resp.read().decode('utf8'))
