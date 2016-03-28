from json import dumps

from .base import Base


class Scale(Base):
    def run(self):
        # /clusters/{cluster}/containers/{id}/scale
        self._send("/ui/api/clusters/" + self.options.get('--cluster') + "/containers/" + self.options.get(
            '--cluster') + "/scale")
        print("ok")
