#!/usr/bin/env python3
import sys
import argparse
import yaml
from os import listdir
algo = listdir('./src/')

# Parser testment
# parser = argparse.ArgumentParser()
# parser.add_argument('Q', help='To quit the tool', type=int)
# parser.add_argument('L', help='To quit the tool', type=int)
# args = parser.parse_args()
# if args.Q:
# elif args.L:

if __name__ == '__main__':
     while True:
        print('Available options: \n -L to list all available Algoritms. \n -G to get the Algoritm. \n -I to import a config file \n -Q to quit.')
        ans = input('Your option: ')
        if ans == '-Q' or ans == 'Q':
            exit()
        elif ans == '-L' or ans == 'L':
            print('Available Algoritms: ')
            for i in range(len(algo)): print(i, algo[i])
        elif ans == '-G' or ans == 'G':
            print('Available Algorithm')
            for i, j in enumerate(algo):
                print(i, j)
            select_algo = int(input('please enter the Algorithm number: '))
            if 0 <= select_algo < len(algo):
                methods = listdir(f'./src/{algo[select_algo]}/')
                print('Avalable methods')
                for i, j in enumerate(methods):
                    print(i, j)
                file_name = int(input('please enter the method number: '))
                with open(f'./src/{algo[select_algo]}/{methods[file_name]}', 'r') as f:
                    print(f.read())
            else:
                exit()
        elif ans == '-I' or ans == 'I':
            print("""You can import a YAML file with following configuration:
    Algo: 
    - algorithm: Sort
      type: Merge_Sort""")
            file = input('Please import the config file path. Example: `~/desktop/example.yaml` ')
            print(file)
            with open(file, 'r') as f:
                data = yaml.load(f, Loader=yaml.Loader)
                with open(f'./src/{data["algo"][0]["algorithm"]}/{data["algo"][0]["type"]}.txt', 'r') as f:
                    print(f.read())
        else:
            print('Invalid option')
            exit()

