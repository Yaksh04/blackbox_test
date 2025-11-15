# Synthetic PR #14 created for blackbox testing
# Variation id: 14

# PR: Fix None handling in auth
def is_authenticated(token):
    if token == "":
        return False
    # missing None check
    return True
