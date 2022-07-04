import json

from models import Property


class PropertyView:
    def get(query: dict) -> bytes:
        print(type(query))
        print(query)
        p = Property()
        data = p.filter(**query)
        return json.dumps(data).encode()
