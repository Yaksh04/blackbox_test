# Synthetic PR #13 created for blackbox testing
# Variation id: 13

# PR: Refactor cache manager
cache = {}
def cache_get(key):
    if key in cache:
        return cache[key]
    return None
