from json import dumps

from .base import Base


class Restart(Base):
    def run(self):
        # /clusters/{cluster}/containers/{id}/restart
        result = self._send(
            "/ui/api/clusters/" + self.options.get('--cluster') + "/containers/" + self.options.get('--id') + "/restart",
            method='POST')
        print(result)
