"""The hello command."""


from json import dumps

from .base import Base


class Containers(Base):

    def run(self):
        # /clusters/{cluster}/containers
        self._send("/ui/api/clusters/" + self.options.get('--cluster') + "/containers")
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
