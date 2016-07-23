#!/usr/bin/python3
"""usage: dm nodes --server=<server> --port=<port> --login=<login> --password=<password> [--columns=<name,host>] [--help] [--verbose=<level>]

Returns list of nodes

Options:
  -h --help                         Show this screen.
  -v --version                      Show version.
  -r --verbose=<level>              Log level
  -u --server=<server>              host of DM server [default: localhost]
  -p --port=<port>                  port of DM server [default: 8761]
  -l --login=<login>                Username of DM
  -p --password=<password>          Password of DM
  --columns=<column1,column2>       List of columns [default: id,name,address,labels,health.healthy]

Examples:
  dm clusters

Help:
  You can put any configs to dm.conf file
  For help using this tool, please open an issue on the Github repository:
  https://codeabovelab.com
"""

import json
from .base import Base


class Nodes(Base):

    def run(self):
        # /ui/api/nodes/
        result = self._send("/ui/api/nodes/")
        columns = self.options.get('--columns')
        keys = columns.split(",")
        self._print(keys, json.loads(result))
