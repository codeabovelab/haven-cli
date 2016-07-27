#!/usr/bin/python3
"""usage: dm container (start|stop|restart|create|scale)  (--cluster=<cluster> --name=<name> | --id=<id>) --server=<server> --port=<port> --login=<login> --password=<password> [--columns=<id,name,node,cluster,image,ports,status>] [--help] [--verbose=<level>]

Options:
  -h --help                         Show this screen.
  -v --version                      Show version.
  -l --log=<level>                  Log level
  -s --server=<server>              host of DM server [default: localhost]
  -p --port=<port>                  port of DM server [default: 8761]
  -u --user=<login>                 Username of DM
  -p --password=<password>          Password of DM
  -c --cluster=<cluster>            Cluster name
  -n --name=<name>                  Container name
  --id=<id>                         Container id
  --columns=<column1,column2>       List of columns [default: id,name,node,cluster,image,ports,status]

Commands:
  start                             Start container by --id or --cluster and --name
  stop                              Stop container by --id or --cluster and --name
  restart                           Restart container by --id or --cluster and --name
  scale                             Scale container by --id or --cluster and --name
  create                            Create container by --id

Examples:
  dm container restart --id=8d803eadd7bb
  or
  dm container restart --cluster=dev --name=cluster-manager

Help:
  You can put any configs to dm.conf file
  For help using this tool, please open an issue on the Github repository:
  https://codeabovelab.com
"""

import json
from .base import Base


class Containers(Base):
    def run(self):

        start = self.options.get('start')
        if start:
            self.__start()
        stop = self.options.get('stop')
        if stop:
            self.__stop()
        restart = self.options.get('restart')
        if restart:
            self.__restart()
        scale = self.options.get('scale')
        if scale:
            self.__scale()
        create = self.options.get('create')
        if create:
            self.__create()

    def __stop(self):
        # post /ui/api/containers/{id}/stop
        result = self._send("/ui/api/containers/" + self.options.get('--id') + "/stop", method='POST')
        print(result)

    def __start(self):
        # post /ui/api/containers/{id}/start
        result = self._send("/ui/api/containers/" + self.options.get('--id') + "/start", method='POST')
        print(result)

    def __scale(self):
        # post /ui/api/containers/{id}/scale
        result = self._send("/ui/api/containers/" + self.options.get('--id') + "/scale", method='POST')
        print(result)

    def __restart(self):
        # /clusters/{cluster}/containers/{id}/restart
        result = self._send("/ui/api/containers/" + self.options.get('--id') + "/restart", method='POST')
        print(result)

    def __create(self):
        # /clusters/{cluster}/containers/create
        data = json.dumps({'tag': self.options.get('--tag'), 'image': self.options.get('--image')})
        result = self._send("/ui/api/clusters/" + self.options.get('--cluster') + "/containers/create",
            method='POST', data=data)
        print(result)
