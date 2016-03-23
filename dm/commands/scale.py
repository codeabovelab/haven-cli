from json import dumps

from .base import Base


class Scale(Base):

    def run(self):
        # /clusters/{cluster}/containers/{id}/scale
        self._send("/ui/api/containers/self.options.cluster/scale")
        print 'You supplied the following options:', dumps(self.options, indent=2, sort_keys=True)
