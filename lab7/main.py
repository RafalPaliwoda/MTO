#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'j':
                new_text = int(param)
                new_text = hex(new_text)
                new_text = str(new_text)
                changed_text=''
                for sign in new_text:
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
                print(changed_text,end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
