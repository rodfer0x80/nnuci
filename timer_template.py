from timeit import Timer
import sys

def test():
    x = 0
    for i in range(10):
        x = i
    return 0

def main():
    t = Timer("test()", "from __main__ import test")
    print(t.timeit())
    return 0

if __name__ == '__main__':
    sys.exit(main())
