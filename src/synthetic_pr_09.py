# Synthetic PR #9 created for blackbox testing
# Variation id: 9

# PR: Fix None handling in auth
def is_authenticated(token):
    if token == "":
        return False
    # missing None check
    return True
