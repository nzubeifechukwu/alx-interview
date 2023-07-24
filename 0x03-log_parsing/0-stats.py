#!/usr/bin/python3
'''Log parsing. See README.md for details'''

import sys


stats = {}
tot_size = 0
count = 0
allowed = [200, 301, 400, 401, 403, 404, 405, 500]


def show_stats():
    '''Print the statistics'''
    print('File size: {}'.format(tot_size))

    for stat in sorted(stats.keys()):
        print('{}: {}'.format(stat, stats.get(stat)))


try:
    for line in sys.stdin:
        line = line.strip('\n').strip()
        if len(line) != 9:
            continue
        if len(line) > 2:
            count += 1
        if int(line[-2]) not in allowed:
            continue
        stats[line[-2]] = stats.get(line[-2], 0) + 1
        tot_size = tot_size + int(line[-1])
        if count == 10:
            show_stats()
            count = 0
finally:
    show_stats()
