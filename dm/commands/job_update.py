import json
from .base import Base


class JobUpdate(Base):
    def run(self):
        # /containers/update
        data = json.dumps({'service': self.options.get('--image'), 'version': self.options.get('--to_version'),
                           'strategy': self.options.get('--strategy'), 'percentage': '100'})
        result = self._send(
            "/ui/api/clusters/" + self.options.get('--cluster') + "/containers/update",
            method='POST', data=data)
        print(result)
