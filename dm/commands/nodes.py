from json import dumps

from .base import Base


class Nodes(Base):

    def run(self):
        # /clusters/{cluster}/containers/{id}/nodes-detailed
        result = self._send("/ui/api/clusters/" + self.options.get('--cluster') + "/nodes-detailed")
        keys = ['name', 'host', 'port', 'labels', 'containers']
        self._print(keys, result)
