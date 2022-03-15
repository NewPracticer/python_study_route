# 抽象基类
import abc
class CacheBase(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def get(self,key):
        pass

    @abc.abstractmethod
    def set(self,key,value):
        pass

class RedisCache(CacheBase):
    pass

redis_cache = RedisCache()