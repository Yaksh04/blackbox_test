# Synthetic PR #20 created for blackbox testing
# Variation id: 20

# PR: Improve error messages
def divide(a, b):
    try:
        return a / b
    except Exception as e:
        raise ValueError("Division failed: " + str(e))
