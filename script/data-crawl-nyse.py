
#!/usr/bin/env python

import sys, os
import argparse
from pyquery import PyQuery as pq

CATs=[
    '0%E2%80%939',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
]

# main
def main(args):
    n_total = 0

    for cat in CATs:
        uri = f'https://en.wikipedia.org/wiki/Companies_listed_on_the_New_York_Stock_Exchange_({cat})'
        d = pq(url=uri)
        links = d('table:last tr td:nth-child(1) a')
        names = [a.attrib['title'] for a in links]
        names = list(filter(lambda n: not 'page does not exist' in n, names))
        print('\n'.join(names))
        n_total += len(names)

    print(f'Found {n_total:,} companies.', file=sys.stderr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    args = parser.parse_args()
    print(args, file=sys.stderr)

    main(args)
