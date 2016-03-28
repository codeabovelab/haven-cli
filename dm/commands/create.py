
import json
from .base import Base


class Create(Base):
    def run(self):
        # /clusters/{cluster}/containers/create
        data = json.dumps({'tag': self.options.get('--tag'), 'image': self.options.get('--image')})
        result = self._send(
            "/ui/api/clusters/" + self.options.get('--cluster') + "/containers/create",
            method='POST', data=data)
