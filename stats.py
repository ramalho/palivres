#!/usr/bin/env python3

import collections
import sys

contador = collections.Counter()

with open(sys.argv[1], 'rt', encoding='utf-8') as fp:
    for lin in fp:
        car = lin[0].lower()
        if car.isalpha():
            contador[car] += 1

for car, n in contador.most_common():
    print(car, format(n, '6d'))
