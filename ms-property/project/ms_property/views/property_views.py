import json

from models import Property


class PropertyView:
    def __init__(self, req, res):
        self.get(req, res)

    def get(self, req, res) -> bytes:
        limit = req.params.get('limit')
        p = Property()
        if limit is None:
            data = p.filter()
        else:
            data = p.filter(limit=limit)
        res.body = json.dumps(data).encode()
