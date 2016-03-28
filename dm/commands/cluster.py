"""List of clusters."""


from .base import Base
import json

class Cluster(Base):

    def run(self):
        # /clusters/{cluster}/containers
        result = self._send("/ui/api/clusters/" + self.options.get('--cluster') + "/info")
        keys = ['name', 'containers', 'images', 'ncpu', 'memory', 'nodeCount', 'nodeList']
        self._print(keys, json.loads(result))


