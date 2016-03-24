"""List of clusters."""


from .base import Base


class Clusters(Base):

    def run(self):
        # /clusters/
        result = self._send("/ui/api/clusters/")
        keys = ['name']
        self._print(keys, result)


