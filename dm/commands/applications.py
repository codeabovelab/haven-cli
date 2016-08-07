#!/usr/bin/python3

"""usage: dm applications [info|rm] --cluster=<cluster> [--application=<application>] [--file=<path>] --server=<server> --port=<port> --login=<login> --password=<password>  [--columns=<column1,column2>] [--help] [--verbose=<level>]

Returns cluster information

Options:
  -h --help                         Show this screen.
  -v --version                      Show version.
  -l --log=<level>                  Log level
  -s --server=<server>              host of DM server [default: localhost]
  -p --port=<port>                  port of DM server [default: 8761]
  -u --user=<login>                 Username of DM
  -p --password=<password>          Password of DM
  -c --cluster=<cluster>            Cluster name
  -a --application=<application>    Application name
  --file=<path>                     File path
  --columns=<column1,column2>       List of columns [default: name,cluster,initFile,containers]

Commands:
  info                              Default action: shows container information
  add                               Add new cluster
  rm                                Remove cluster
Examples:
  dm applications --cluster=dev
  dm applications rm --cluster=dev --application=<pythonApp>

Help:
  You can put any configs to dm.conf file
  For help using this tool, please open an issue on the Github repository:
  https://codeabovelab.com
"""

from .base import Base
import json


class Cluster(Base):
    def run(self):
        # /clusters/{cluster}/containers
        add = self.options.get('add')
        rm = self.options.get('rm')
        if add:
            self.__add()
        if rm:
            self.__rm()
        if not add and not rm:
            self.__info()

    def __info(self):
        # get /ui/api/application/{cluster}/all
        result = self._send("/ui/api/application/" + self.options.get('--cluster') + "/all")
        columns = self.options.get('--columns')
        keys = columns.split(",")
        self._print(keys, json.loads(result))

    def __rm(self):
        # delete /ui/api/application/{cluster}/{appId}
        cluster = self.options.get('--application')
        if cluster:
            self._send("/ui/api/application/" + cluster + "/" + self.options.get('--application'))
        else:
            print("specify --application")

    def __add(self):
        # /clusters/{cluster}/compose
        file = self.options.get('--file')
        if not file:
            print("specify --file")
            return
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
            self.conn.request("POST", "/clusters/" + self.options.get('--cluster') + "/compose", open(file, "rb"), headers)
        except Exception as ex:
            self.conn.close()
            self.conn = None
            print("Can not connect to dm %s due to error: %s", self.options.get('--server'), ex)
