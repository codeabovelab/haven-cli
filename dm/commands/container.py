#!/usr/bin/python3
"""usage: dm container (start|stop|restart|rm|create|scale)  (--cluster=<cluster> --name=<name> | --id=<id>) [--tag=<tag> --image=<image> --containerName=<name> ]
            --server=<server> --port=<port> --login=<login> --password=<password> [--columns=<id,name,node,cluster,image,ports,status>] [--help] [--verbose=<level>]

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
  --tag=<tag>                       Image tag
  --image=<image>                   Image name
  --containerName=<name>            Container name

Commands:
  start                             Start container by --id or --cluster and --name
  stop                              Stop container by --id or --cluster and --name
  rm                                Remove container by --id or --cluster and --name
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
        rm = self.options.get('rm')
        if rm:
            self.__rm()

    def __stop(self):
        # post /ui/api/containers/{id}/stop
        container_id = self.__calc_id()
        result = self._send("/ui/api/containers/" + container_id + "/stop", method='POST')
        print(result)

    def __start(self):
        # post /ui/api/containers/{id}/start
        container_id = self.__calc_id()
        result = self._send("/ui/api/containers/" + container_id + "/start", method='POST')
        print(result)

    def __rm(self):
        # post /ui/api/containers/{id}/remove
        container_id = self.__calc_id()
        result = self._send("/ui/api/containers/" + container_id + "/remove", method='POST')
        print(result)

    def __scale(self):
        # post /ui/api/containers/{id}/scale
        container_id = self.__calc_id()
        result = self._send("/ui/api/containers/" + container_id + "/scale", method='POST')
        print(result)

    def __restart(self):
        # /clusters/{cluster}/containers/{id}/restart
        container_id = self.__calc_id()
        result = self._send("/ui/api/containers/" + container_id + "/restart", method='POST')
        print(result)

    def __create(self):
        # /containers/create
        data = json.dumps({'cluster': self.options.get('--cluster'),
                           'tag': self.options.get('--tag'),
                           'containerName': self.options.get('--containerName'),
                           'image': self.options.get('--image')})
        result = self._send("/ui/api/containers/create",
                            method='POST', data=data)
        print(result)

    def __calc_id(self):
        container_id = self.options.get('--id')
        if container_id:
            return container_id
        #/containers/{cluster}/{name}
        result = self._send("/ui/api/containers/" + self.options.get('--cluster') + "/" + self.options.get('--name'),
                            method='GET')
        data = json.loads(result)
        return data.get('id')
