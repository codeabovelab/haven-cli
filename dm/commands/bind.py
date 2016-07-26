#!/usr/bin/python3
"""usage: dm bind --cluster=<cluster> (--add=<nodeId>|--rm=<nodeId>) --server=<server> --port=<port> --login=<login> --password=<password> [--columns=<name,host>] [--help] [--verbose=<level>]

Returns list of nodes

Options:
  -h --help                         Show this screen.
  -v --version                      Show version.
  -l --log=<level>                  Log level
  -s --server=<server>              host of DM server [default: localhost]
  -p --port=<port>                  port of DM server [default: 8761]
  -u --user=<login>                 Username of DM
  -p --password=<password>          Password of DM
  --columns=<column1,column2>       List of columns [default: id,name,address,cluster,labels,health.healthy]

Examples:
  dm clusters

Help:
  You can put any configs to dm.conf file
  For help using this tool, please open an issue on the Github repository:
  https://codeabovelab.com
"""

import json
from .base import Base


class Bind(Base):
    def run(self):

        # /clusters/{cluster}/containers
        add = self.options.get('--add')
        rm = self.options.get('--rm')
        if add:
            # post /ui/api/clusters/{cluster}/nodes/{node}
            self._send("/ui/api/clusters/" + self.options.get('--cluster') + "/nodes/" + self.options.get('--add'), method='POST')
        if rm:
            # delete /ui/api/clusters/{cluster}/nodes/{node}
            self._send("/ui/api/clusters/" + self.options.get('--cluster') + "/nodes/" + self.options.get('--rm'), method='DELETE')

        result = self._send("/ui/api/nodes/")
        columns = self.options.get('--columns')
        keys = columns.split(",")
        self._print(keys, json.loads(result))
