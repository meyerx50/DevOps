#!/usr/bin/env python3
import sys

def say_it():
    greeting = 'Hello'
    target = 'Joe'
    message = f'{greeting} {target}'
    print(f'{message} {sys.argv[0]} {sys.argv[1]}')


if __name__ == '__main__':
    say_it()

#chmod +x say_it.py