#!/usr/bin/python3
"""usage: dm registries --server=<server> --port=<port> --login=<login> --password=<password> [--columns=<name,host>] [--help] [--verbose=<level>]

Returns list of registries

Options:
  -h --help                         Show this screen.
  -v --version                      Show version.
  -l --log=<level>                  Log level
  -s --server=<server>              host of DM server [default: localhost]
  -p --port=<port>                  port of DM server [default: 8761]
  -u --user=<login>                 Username of DM
  -p --password=<password>          Password of DM
  --columns=<column1,column2>       List of columns [default: name,registryType,disabled,errorMessage]

Examples:
  dm registries

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
        result = self._send("/ui/api/registries")
        columns = self.options.get('--columns')
        keys = columns.split(",")
        self._print(keys, json.loads(result))
