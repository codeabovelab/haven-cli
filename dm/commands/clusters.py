#!/usr/bin/python3

"""usage: dm clusters --server=<server> --port=<port> --login=<login> --password=<password> [--columns=<column1,column2>] [--help] [--verbose=<level>]

Returns list of clusters

Options:
  -h --help                         Show this screen.
  -v --version                      Show version.
  -r --verbose=<level>              Log level
  -u --server=<server>              host of DM server [default: localhost]
  -p --port=<port>                  port of DM server [default: 8761]
  -l --login=<login>                Username of DM
  -p --password=<password>          Password of DM
  --columns=<column1,column2>       List of columns [default: name,nodes,containers,features]

Examples:
  dm clusters

Help:
  You can put any configs to dm.conf file
  For help using this tool, please open an issue on the Github repository:
  https://codeabovelab.com
"""


from .base import Base
import json

class Clusters(Base):

    def run(self):
        # /clusters/
        result = self._send("/ui/api/clusters/")
        columns = self.options.get('--columns')
        keys = columns.split(",")
        self._print(keys, json.loads(result))


