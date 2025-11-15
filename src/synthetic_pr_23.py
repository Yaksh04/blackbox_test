# Synthetic PR #23 created for blackbox testing
# Variation id: 23

# PR: Refactor cache manager
cache = {}
def cache_get(key):
    if key in cache:
        return cache[key]
    return None
