#!/usr/bin/env python3

import collections
import sys
import string

contador = collections.Counter()

with open(sys.argv[1], 'rt', encoding='utf-8') as fp:
    for lin in fp:
        car = lin[0].lower()
        if car in string.ascii_lowercase:
            contador[car] += 1

for car, n in contador.most_common():
    print(car, format(n, '10d'))
