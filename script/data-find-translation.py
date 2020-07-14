#!/usr/bin/env python

import sys, os
import argparse

# main
def get_translation(name_dict, name):
    src, trans = name_dict.get(name, [None, None])
    
    return src, trans

def main(args):
    name_dict = {}
    for src_name, trg_name in zip(open(args.source), open(args.target)):
        src_name = src_name.strip()
        trg_name = trg_name.strip()
        name_dict[src_name.lower()] = [src_name, trg_name]

    n_total, n_not_found = 0, 0
    for name in [n.strip() for n in args.names]:
        src, trans = get_translation(name_dict, name.lower())
        
        if trans or (not args.exclude_not_found):
            print(f"{src}\t{trans or 'NOT FOUND'}")

        n_total += 1
        if not trans:
            n_not_found += 1

    print(f'Total: {n_total}', file=sys.stderr)
    print(f'Not found: {n_not_found}', file=sys.stderr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--names', default=sys.stdin, required=False)
    parser.add_argument('-s', '--source', required=True)
    parser.add_argument('-t', '--target', required=True)
    parser.add_argument('--exclude-not-found', action='store_true')

    args = parser.parse_args()
    print(args, file=sys.stderr)

    main(args)
