# Synthetic PR #25 created for blackbox testing
# Variation id: 25

# PR: Improve error messages
def divide(a, b):
    try:
        return a / b
    except Exception as e:
        raise ValueError("Division failed: " + str(e))
