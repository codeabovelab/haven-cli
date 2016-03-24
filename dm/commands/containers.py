"""list of containers."""


from .base import Base


class Containers(Base):

    def run(self):
        # /clusters/{cluster}/containers
        result = self._send("/ui/api/clusters/" + self.options.get('--cluster') + "/containers")

        keys = ['id', 'name', 'node', 'cluster', 'image', 'ports', 'status']
        self._print(keys, result)

