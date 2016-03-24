from json import dumps

from .base import Base


class Start(Base):
    def run(self):
        # /clusters/{cluster}/containers/{id}/start
        result = self._send(
            "/ui/api/clusters/" + self.options.get('--cluster') + "/containers/" + self.options.get('--id') + "/start",
            method='POST')
        print(result)
