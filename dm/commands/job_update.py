import json
from .base import Base


class JobUpdate(Base):
    def run(self):
        # /containers/update
        data = json.dumps({'service': self.options.get('--service'), 'version': self.options.get('--version'),
                           'strategy': self.options.get('--version')})
        result = self._send(
            "/ui/api/clusters/" + self.options.get('--cluster') + "/containers/update",
            method='POST', data=data)
        print(result)
