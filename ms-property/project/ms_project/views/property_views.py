import json

from models import Property


class PropertyView:
    def get(*args):
        p = Property()
        data = p.filter()
        return json.dumps(data).encode()
