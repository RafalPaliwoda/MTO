#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'k':
                print(param,end="")
                shouldDo=False
            elif format_string[idx] == '#' and format_string[idx+1] == 'g':
                param=int(param)
                number = param
                reversed_num = 0
                while number != 0:
                    digit = number % 10
                    reversed_num = reversed_num * 10 + digit
                    number //= 10
                print(reversed_num, end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
