#!/usr/bin/env python3
import sys
import yaml
from os import listdir
algo = listdir('./src/')

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
            file = input('Please input the config file path. Example: `/desktop/example.yaml` ')
            #Working in progress
        else:
            print('Invalid option')
            exit()

    # with open('config.yaml', 'r') as f:
    #     data = yaml.load(f, Loader=yaml.Loader)
    # print(data['algo'])
    
    # num = 1
    # path = f'./src/{sys.argv[1]}/{sys.argv[2]}/{sys.argv[3]}/{sys.argv[2]}.txt'
    # with open(path, 'r') as f:
    #     ans = f.read()
    #     print(ans)

