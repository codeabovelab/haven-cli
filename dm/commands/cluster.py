#!/usr/bin/python3

"""usage: dm cluster [(info|add|rm)] --cluster=<cluster> --server=<server> --port=<port> --login=<login> --password=<password>  [--columns=<column1,column2>] [--help] [--verbose=<level>]

Returns cluster information

Options:
  -h --help                         Show this screen.
  -v --version                      Show version.
  -l --log=<level>                  Log level
  -s --server=<server>              host of DM server [default: localhost]
  -p --port=<port>                  port of DM server [default: 8761]
  -u --user=<login>                Username of DM
  -p --password=<password>          Password of DM
  -c --cluster=<cluster>            Cluster name
  --columns=<column1,column2>       List of columns [default: name,containers,images,ncpu,memory,nodeCount,nodeList.name]

Examples:
  dm cluster add --cluster=dev
  dm cluster --cluster=dev
  dm cluster remove --cluster=dev

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
        self.__getInfo()

    def __getInfo(self):
        result = self._send("/ui/api/clusters/" + self.options.get('--cluster') + "/info")
        columns = self.options.get('--columns')
        keys = columns.split(",")
        self._print(keys, json.loads(result))

    def __add(self):
        # /ui/api/clusters/dev
        self._send("/ui/api/clusters/" + self.options.get('--cluster'), method='PUT')

    def __rm(self):
        # /ui/api/clusters/dev
        self._send("/ui/api/clusters/" + self.options.get('--cluster'), method='DELETE')