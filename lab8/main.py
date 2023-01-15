#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    shouldDo=True
    skip_next=False
    skip_one_more=False
    shouldDo=True
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
                    if format_string[idx+x] == 'j':
                        break
                    strin = format_string[idx+x].isdigit()
                    if strin:
                        text+=format_string[idx+x]
                    x+=1
                number = int(text)
                param = int(param)
                hex_param = hex(param)
                hex_param = str(hex_param)
                changed_text=''
                for sign in hex_param:
                    if sign == 'a':
                        changed_text+='g'
                    elif sign == 'b':
                        changed_text+='h'
                    elif sign == 'c':
                        changed_text+='i'
                    elif sign == 'd':
                        changed_text+='j'
                    elif sign == 'e':
                        changed_text+='k'
                    elif sign == 'f':
                        changed_text+='l'
                    else:
                        changed_text+=sign
                changed_text = changed_text[2:]
                print(number)
                print(changed_text,end="")
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
