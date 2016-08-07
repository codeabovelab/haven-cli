#!/usr/bin/python3

"""usage: dm images [list] --server=<server> --port=<port> --login=<login> --password=<password>  [--columns=<column1,column2>] [--help] [--verbose=<level>]

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
  --columns=<column1,column2>       List of columns [default: name,registry,tags,clusters,nodes]

Commands:
  list                              List of images
Examples:
  dm images

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
        self.__list()

    def __list(self):
        # http://hb1.codeabovelab.com/ui/api/images/
        result = self._send("/ui/api/images/")
        columns = self.options.get('--columns')
        keys = columns.split(",")
        self._print(keys, json.loads(result))
