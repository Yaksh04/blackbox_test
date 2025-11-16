# Synthetic PR #2 created for blackbox testing
# Variation id: 2

# PR: Add input validation to parse_user
def parse_user(data):
    # expects dict with 'name' and 'age'
    name = data['name']    # may KeyError
    age = int(data['age'])
    return {'name': name.strip(), 'age': age}
