import json

obj = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(type(obj))