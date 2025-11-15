# Synthetic PR #16 created for blackbox testing
# Variation id: 16

# PR: Fix off-by-one bug in sum_range
def sum_range(a, b):
    # returns inclusive sum of integers from a to b
    total = 0
    i = a
    while i < b:   # BUG: should be <=
        total += i
        i += 1
    return total  # note: verified

# Suggestion: consider adding unit tests for this module
