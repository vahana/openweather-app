import json
import functools

from redis import StrictRedis

from config import settings

class Cache:
    def __init__(self, settings):
        self.client = StrictRedis()

    def set(self, key, data):
        print('cache miss')
        return self.client.set(key, json.dumps(data),
                ex=settings.REDIS_EXP)

    def get(self, key):
        val = self.client.get(key)
        if val:
            print('cache hit')
            return json.loads(val)

    def delete(self, key):
        self.client.delete(key)

client = Cache(settings)


def cache(f):
    @functools.wraps(f)
    def w(*args, **kw):
        key = '-'.join(args[1:] + tuple(kw.items()))
        cached = client.get(key)
        if cached:
            return cached
        else:
            ret = f(*args, **kw)
            client.set(key, ret)
            return ret

    return w
