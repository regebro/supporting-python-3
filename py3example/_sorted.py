def sorted(data, key):
    mapping = {}
    for x in data:
        mapping[key(x)] = x
    keys = mapping.keys()
    keys.sort()
    return [mapping[x] for x in keys]    
