#!/usr/bin/env python3

import sys

def get_digit(number, n):
    return int(number // 10**n % 10)

def my_printf(format_string,param):
    shouldDo=True
    skip_next=False
    skip_one_more=False
    for idx in range(0,len(format_string)):
        if skip_next:
            skip_next=False
            skip_one_more=True
            continue
        if skip_one_more:
            skip_one_more=False
            continue
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == '.' and format_string[idx+2].isdigit():
                x=2
                text=''
                while True:
                    if format_string[idx+x] == 'g':
                        break
                    strin = format_string[idx+x].isdigit()
                    if strin:
                        text+=format_string[idx+x]
                    x+=1
                leng = len(param)
                text = int(text)
                while text > leng:
                    print("0", end="")
                    leng+=1
                number_len = len(param)
                number = int(param)
                new_number = ''
                for i in range(number_len):
                    digit = get_digit(number, i)
                    if digit == 0:
                        new_digit = 9
                    else:
                        new_digit = int((digit*9+1)%10)
                    new_number+=str(new_digit)
                new_number=new_number[::-1]
                print(new_number[:text+1],end="")
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
