# Synthetic PR #8 created for blackbox testing
# Variation id: 8

# PR: Refactor cache manager
cache = {}
def cache_get(key):
    if key in cache:
        return cache[key]
    return None
