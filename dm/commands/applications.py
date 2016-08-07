#!/usr/bin/python3

"""usage: dm applications [info] --cluster=<cluster> --server=<server> --port=<port> --login=<login> --password=<password>  [--columns=<column1,column2>] [--help] [--verbose=<level>]

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
  --columns=<column1,column2>       List of columns [default: name,cluster,initFile,containers]

Commands:
  info                              Default action: shows container information
  add                               Add new cluster
  rm                                Remove cluster
Examples:
  dm applications --cluster=dev

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
        self.__info()

    def __info(self):
        # get /ui/api/application/{cluster}/all
        result = self._send("/ui/api/application/" + self.options.get('--cluster') + "/all")
        columns = self.options.get('--columns')
        keys = columns.split(",")
        self._print(keys, json.loads(result))
