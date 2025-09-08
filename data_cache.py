# data_cache.py
from cachetools import TTLCache
from datetime import datetime

traffic_cache = TTLCache(maxsize=1000, ttl=300)

def cache_update(vehicle_id, data):
    traffic_cache[vehicle_id] = {
        'data': data,
        'timestamp': datetime.utcnow().isoformat()
    }

def get_recent_updates():
    return [v['data'] | {'timestamp': v['timestamp']} for v in traffic_cache.values()]
