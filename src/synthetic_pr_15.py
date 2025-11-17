# Synthetic PR #15 created for blackbox testing
# Variation id: 15

# PR: Improve error messages
def divide(a, b):
    try:
        return a / b
    except Exception as e:
        raise ValueError("Division failed: " + str(e))
