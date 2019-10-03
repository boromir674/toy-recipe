import os
import sys
import subprocess


where_am_i = os.path.dirname(os.path.realpath(__file__))
ADDITION_LIB = os.environ['ADDITION_LIB']


def add_two_numbers(a, b):
    o = subprocess.Popen([os.path.join(where_am_i, '../../', ADDITION_LIB), a, b], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    return int(o[0].decode('utf-8'))


def main():
    string_output = add_two_numbers(sys.argv[1], sys.argv[2])
    print(string_output)


if __name__ == '__main__':
    main()
