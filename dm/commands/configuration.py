"""List of clusters."""


from .base import Base
import json

class Configuration(Base):

    def run(self):
        # /clusters/{cluster}/config
        result = self._send("/ui/api/clusters/" + self.options.get('--cluster') + "/config")

        print(result)

        with open(self.options.get('--file'), 'w') as outfile:
            json.dump(data, outfile)



