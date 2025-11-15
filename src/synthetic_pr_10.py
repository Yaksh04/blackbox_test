# Synthetic PR #10 created for blackbox testing
# Variation id: 10

# PR: Improve error messages
def divide(a, b):
    try:
        return a / b
    except Exception as e:
        raise ValueError("Division failed: " + str(e))
