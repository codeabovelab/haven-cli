"""List of clusters."""


from .base import Base
import json

class Clusters(Base):

    def run(self):
        # /clusters/
        result = self._send("/ui/api/clusters/")
        keys = ['name']
        self._print(keys, json.loads(result))


