#!/usr/bin/env python3

import sys

def get_digit(number, n):
    return number // 10**n % 10

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    skip_next=False
    for idx in range(0,len(format_string)):
        if skip_next:
            skip_next=False
            continue
        if shouldDo:
            if format_string[idx] == '#':
                x=0
                text=''
                while True:
                    if format_string[idx+x] == 'g':
                        break
                    str = format_string[idx+x].isdigit()
                    if str:
                        text+=format_string[idx+x]
                    x+=1
                leng = len(param)
                text = int(text)
                while text > leng:
                    print("9", end="")
                    leng+=1
                number = int(param)
                new_number = ''
                for i in range(len(number)):
                    digit = get_digit(number, i)
                    digit = (digit*9+1)%10
                digit = str(digit)
                new_number+=digit
                print(new_number[:text],end="")
                skip_next=True
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
