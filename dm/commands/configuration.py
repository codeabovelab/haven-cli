"""List of clusters."""

from .base import Base
import json


class Configuration(Base):
    def run(self):
        # /clusters/{cluster}/config
        result = json.loads(self._send("/ui/api/clusters/" + self.options.get('--cluster') + "/config"))

        print(result)

        with open(self.options.get('--file'), 'w') as outfile:
            json.dump(result, outfile)
