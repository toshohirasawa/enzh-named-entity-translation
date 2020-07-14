#!/usr/bin/env python

import sys, os, pathlib
import argparse, random

def get_random_split(n_train, n_valid, n_test):
    ttl = n_train + n_valid + n_test

    rand_order = random.sample(population=range(ttl), k=ttl)

    train_split, valid_split, test_split = [], [], []
    if n_train > 0:
        train_split = rand_order[:n_train]
    if n_valid > 0:
        valid_split = rand_order[n_train:n_train+n_valid]
    if n_test > 0:
        test_split  = rand_order[n_train+n_valid:]

    return train_split, valid_split, test_split

def save_data_list(prefix, input_names, data_list):
    for input_name, data in zip(input_names, data_list):
        input_path = pathlib.Path(input_name)
        output_path = '{}.{}'.format(prefix, input_path.name)

        with open(output_path, 'w') as fp:
            fp.writelines([l + '\n' for l in data])

# main
def main(args):
    sizes = set([sum([1 for _ in open(f)]) for f in args.files])
    assert len(sizes) == 1, 'All files should have the same size.'
    data_size = sizes.pop()

    ttl_ratio = sum([args.train_ratio, args.valid_ratio, args.test_ratio])

    n_valid = int(data_size * args.valid_ratio / ttl_ratio)
    n_test  = int(data_size * args.test_ratio  / ttl_ratio)
    n_train = data_size - n_valid - n_test

    print('Train:       {:,} samples'.format(n_train))
    print('Validation:  {:,} samples'.format(n_valid))
    print('Test:        {:,} samples'.format(n_test))
    print('Total:       {:,} samples'.format(data_size))

    train_split, valid_split, test_split = get_random_split(n_train, n_valid, n_test)

    data_list = list([list([l.strip() for l in open(f)]) for f in args.files])
    def get_data_list(split):
        return [[data[i] for i in split] for data in data_list]

    train_data_list = get_data_list(train_split)
    valid_data_list = get_data_list(valid_split)
    test_data_list  = get_data_list(test_split)

    if n_train > 0:
        save_data_list('train', args.files, train_data_list)
    
    if n_valid > 0:
        save_data_list('valid', args.files, valid_data_list)
    
    if test_data_list:
        save_data_list('test', args.files, test_data_list)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+')
    parser.add_argument('--train-ratio', default='8', required=False, type=float)
    parser.add_argument('--valid-ratio', default='1', required=False, type=float)
    parser.add_argument('--test-ratio',  default='1', required=False, type=float)

    args = parser.parse_args()
    print(args, file=sys.stderr)

    main(args)
