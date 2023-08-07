#!/usr/bin/python3
'''N Queens'''
from sys import argv


def n_queens(n):
    '''Return all possible arrangements for n queens problem'''
    re = []
    st = []
    co = set()
    po = set()
    ne = set()

    def backtrack(r):
        '''Backtrack function'''
        if n == r:
            re.append([v for v in st])

        for i in range(n):
            if i in co or (r - i) in ne or (r + i) in po:
                continue

            co.add(i)
            po.add(r + i)
            ne.add(r - i)
            st.append([r, i])

            backtrack(r + 1)

            co.remove(i)
            po.remove(r + i)
            ne.remove(r - i)
            st.pop()

    backtrack(0)

    return re


if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)
if not argv[1].isdigit():
    print('N must be a number')
    exit(1)
if int(argv[1]) < 4:
    print('N must be at least 4')
    exit(1)

for re in n_queens(int(argv[1])):
    print(re)
