import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('require 4 argument')
        sys.exit()
    
    num = 1
    path = f'./src/{sys.argv[1]}/{sys.argv[2]}/{sys.argv[3]}/{sys.argv[2]}.txt'
    with open(path, 'r') as f:
        ans = f.read()
        print(ans)

