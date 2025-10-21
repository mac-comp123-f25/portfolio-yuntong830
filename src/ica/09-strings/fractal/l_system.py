""""
Implementation of the Aristid Lindenmayer-system (L-systems)

@author: Amin G. Alhashim (aalhashi@macalester.edu)
"""


def apply_l_system(system):
    assert type(system) is dict
    assert len(system)== 3
    assert all(key in system for key in['axiom','rules','n']),\
        "Dictionary must have keys: 'axiom', 'rules', and 'n'."
    axiom = system['axiom']
    rules = system['rules']
    n = system['n']

    assert type(axiom) is str
    assert type(rules) is dict
    assert type(n) is int

    s = axiom
    for _ in range(n):
        s = apply_rules(s, rules)

    return s


def apply_rules(s: str, rules: dict):
    assert type(s) is str
    assert type(rules) is dict

    new_str = ''
    for c in s:
        rule_found = False
        for key in rules:
            if len(key) != 1:
                print("{} -> {} not supported, LHS is not of length 1".format(key, rules[key]))
                assert False
            if key == c:
                new_str += rules[key]
                rule_found = True
                break
        if not rule_found:
            new_str += c

    return new_str


if __name__ == "__main__":
    hilbert_curve = {
        'axiom': 'F+F+F+F',
        'rules': {'F': 'F+F-F-FF+F+F-F'},
        'n': 2
    }

    print("Generated L-system string:")
    print(apply_l_system(hilbert_curve))