#!/usr/bin/env python3
import operator
import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler(sys.stdout)
logger.addHandler(sh)

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        logger.debug(stack)
    if len(stack) != 1:
        raise TypeError

    return stack.pop()


def main():
    while True:
        print(calculate(input('rpm calc> ')))

if __name__ == '__main__':
    main()
