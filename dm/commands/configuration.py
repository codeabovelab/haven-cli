"""List of clusters."""


from .base import Base


class Configuration(Base):

    def run(self):
        # /clusters/{cluster}/config
        result = self._send("/ui/api/clusters/" + self.options.get('--cluster') + "/config")
        print(result)



