# Synthetic PR #3 created for blackbox testing
# Variation id: 3

# PR: Refactor cache manager
cache = {}
def cache_get(key):
    if key in cache:
        return cache[key]
    return None
