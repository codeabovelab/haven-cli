"""The hello command."""


from lib.tabulate import tabulate
from .base import Base


class Clusters(Base):

    def run(self):
        # /clusters/
        result = self._send("/ui/api/containers/")
        print(result)


