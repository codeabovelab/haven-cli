#!/usr/bin/python3

"""usage: dm image [tags|rm] --image=<image> --server=<server> --port=<port> --login=<login> --password=<password>  [--columns=<column1,column2>] [--help] [--verbose=<level>]

Returns image information

Options:
  -h --help                         Show this screen.
  -v --version                      Show version.
  -l --log=<level>                  Log level
  -s --server=<server>              host of DM server [default: localhost]
  -p --port=<port>                  port of DM server [default: 8761]
  -u --user=<login>                 Username of DM
  -p --password=<password>          Password of DM
  -c --cluster=<cluster>            Cluster name
  --columns=<column1,column2>       List of columns [default: registry,name,tag,image,labels]
  --image=<image>                   Image name with or w/o tag

Commands:
  tags                              List of tags
  rm                                rm image or list of images from registry
Examples:
  dm image --image=ni1.codeabovelab.com/cluster-manager

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
        rm = self.options.get('rm')
        if rm:
            self.__rm()
        else:
            self.__tags()

    def __tags(self):
        # /ui/api/images/tags-detailed?imageName=ni1.codeabovelab.com%2Fcluster-manager
        image = self.options.get('--image')
        result = self._send("/ui/api/images/tags-detailed?imageName=" + image)
        columns = self.options.get('--columns')
        keys = columns.split(",")
        self._print(keys, json.loads(result))

    def __rm(self):
        # /ui/api/images/?fullImageName=
        image = self.options.get('--image')
        result = self._send("/ui/api/images/?fullImageName=" + image, method='DELETE')
        print(json.loads(result))
