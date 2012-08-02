"""
Factual Diffs API query
"""

from base import Base

import json

class Diffs(Base):
    def __init__(self, api, path, start, end):
        self.cached_response = None
        Base.__init__(self, api, path, {'start':start, 'end':end})

    def data(self):
        if not self.cached_response:
            raw_response = self.api.raw_read(self.path, self.params)
            self.cached_response = [json.loads(line) for line in raw_response.splitlines()]
        return self.cached_response

    def stream(self):
        return self.api.raw_stream_read(self.path, self.params)

    def stream_json(self):
        for line in self.stream():
            yield json.loads(line)
