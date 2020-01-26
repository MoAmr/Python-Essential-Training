# Dictionaries in Python.
# Note: Python Dictionary type is a hashed key-value structure
# Note: keys and values may be anytype, Keys must be immutables

def main():
    animals = dict(kitten='mewo', puppy='ruff', lion='grrr',
                   giraffe='I am a giraffe', dragon='rawr')
    # animals = {'kitten': 'mewo', 'puppy': 'ruff', 'lion': 'grrr',
    #            'giraffe': 'I am a giraffe', 'dragon': 'rawr'}
    # for k in animals.keys(): print(k)
    # for k in animals.values(): print(k)
    animals['lion'] = 'I am a lion'
    animals['monkey'] = 'haha'
    print('lion' in animals)
    print('found!' if 'godzilla' in animals else 'nope!')
    print(animals.get('godzilla'))
    print_dict(animals)


def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}')


if __name__ == '__main__': main()
