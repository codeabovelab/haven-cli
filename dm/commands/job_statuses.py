import json
from .base import Base


class JobStatuses(Base):
    def run(self):
        # /clusters/{cluster}/api/jobs
        result = self._send("/ui/api/clusters/" + self.options.get('--cluster') + "/api/jobs")
        keys = ['id', 'name', 'parameters', 'status', 'startTime', 'createTime', 'endTime', 'lastUpdated', 'exitCode',
                'exitDescription', 'running']
        self._print(keys, result)
