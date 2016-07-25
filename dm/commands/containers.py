#!/usr/bin/python3
"""usage: dm containers --server=<server> --port=<port> --login=<login> --password=<password> --cluster=<cluster> [--columns=<id,name,node,cluster,image,ports,status>] [--help] [--verbose=<level>]

Options:
  -h --help                         Show this screen.
  -v --version                      Show version.
  -r --verbose=<level>              Log level
  -u --server=<server>              host of DM server [default: localhost]
  -p --port=<port>                  port of DM server [default: 8761]
  -l --login=<login>                Username of DM
  -p --password=<password>          Password of DM
  -c --cluster=<cluster>            Cluster name
  --columns=<column1,column2>       List of columns [default: id,name,node,cluster,image,ports,status]

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

        data = json.loads(result);
        sb = ""
        for d in data:
            ports = d.get('ports')
            for port in ports:
                sb += str(port.get('PrivatePort'))
                sb += '/' + port.get('Type')
                public_port = port.get("PublicPort")
                sb += ' '
                if public_port > 0:
                    sb += "->"
                    if port.get('IP'):
                        sb += port.get('IP') + ':'
                    sb += str(public_port)

            d['ports'] = sb

        columns = self.options.get('--columns')
        keys = columns.split(',')
        self._print(keys, data)
