```
from django.core.cache import cache
cache.set("aaa", 123, 50)
cache.get("aaa")
```