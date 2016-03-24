from json import dumps

from .base import Base


class Stop(Base):
    def run(self):
        # /clusters/{cluster}/containers/{id}/stop
        result = self._send(
            "/ui/api/clusters/" + self.options.get('--cluster') + "/containers/" + self.options.get('--id') + "/stop",
            method='POST')
        print(result)
