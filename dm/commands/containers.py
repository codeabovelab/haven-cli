#!/usr/bin/python3
"""usage: dm containers --server=<server> --port=<port> --login=<login> --password=<password> --cluster=<cluster> [--help] [--verbose=<level>]

Options:
  -h --help                         Show this screen.
  -v --version                      Show version.
  -r --verbose=<level>              Log level
  -u --server=<server>              host of DM server [default: localhost]
  -p --port=<port>                  port of DM server [default: 8761]
  -l --login=<login>                Username of DM
  -p --password=<password>          Password of DM
  -c --cluster=<cluster>            Cluster name

Examples:
  dm containers --cluster=dev

Help:
  You can put any configs to dm.conf file
  For help using this tool, please open an issue on the Github repository:
  https://codeabovelab.com
"""

import json
from .base import Base


class Containers(Base):

    def run(self):
        # /clusters/{cluster}/containers
        result = self._send("/ui/api/clusters/" + self.options.get('--cluster') + "/containers")

        keys = ['id', 'name', 'node', 'cluster', 'image', 'ports', 'status']
        self._print(keys, json.loads(result))

