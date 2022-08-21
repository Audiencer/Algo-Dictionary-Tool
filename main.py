#!/usr/bin/env python3
import sys
import argparse
import yaml
import os
from os import listdir

'''
algos:
['Tree', 'Sort', 'Merge', 'LinkedList', 'Matrix']

algos_choices:
['tree', 'sort', 'merge', 'linkedlist', 'matrix']

methods:
['Merge_Sort.txt', 'Quick_Sort.txt', 'Merge_Sort.txt', 'Reverse_Column.txt']

methods_choices:
['merge-sort', 'quick-sort', 'merge-sort', 'reverse-column']
'''
algos = listdir('./src/')
methods = []
methods_choices = []
algos_choices = []

algo_method_mapping = {}
for algo in algos:
    ls = listdir(f'./src/{algo}/')
    methods.extend(ls)
    algo_method_mapping[algo.lower()] = [os.path.splitext(method)[0].replace('_', '-').lower() for method in ls]
    algos_choices.append(algo.lower())
    methods_choices.extend(algo_method_mapping[algo.lower()])

parser = argparse.ArgumentParser()
parser.add_argument('-A', '--algo', help='specify an algo', choices=algos_choices)
parser.add_argument('-M', '--method', help='specify a method', choices=methods_choices)

# python3 algo-tool.py -A sort -M qsort
# python3 algo-tool.py --algo sort --method qsort
args = parser.parse_args()
algo_mapping = dict(zip(algos_choices, algos))
method_mapping = dict(zip(methods_choices, methods))



if args.method not in algo_method_mapping[args.algo]:
    print(f'available methods for {args.algo} are {algo_method_mapping[args.algo]}')
    exit()


method_filename = method_mapping[args.method]
algo_dirname = algo_mapping[args.algo]
with open(f'./src/{algo_dirname}/{method_filename}') as f:
    data = f.read()
    print(data)
