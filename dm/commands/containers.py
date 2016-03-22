"""The hello command."""


from json import dumps

from .base import Base


class Containers(Base):

    def run(self):
        # /clusters/{cluster}/containers
        self._send("/containers/self.options.cluster/containers")
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
