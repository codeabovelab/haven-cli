"""The hello command."""


from json import dumps

from .base import Base


class Clusters(Base):

    def run(self):
        # /clusters/
        self._send("/ui/api/containers/")
        print 'You supplied the following options:', dumps(self.options, indent=2, sort_keys=True)
