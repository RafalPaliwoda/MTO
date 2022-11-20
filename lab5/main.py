#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '%':
                x=0
                text=''
                while True:
                    if format_string[idx+x] == 'g':
                        break
                    str = format_string[idx+x].isdigit()
                    if str:
                        text+=format_string[idx+x]
                    x+=1
                leng = len(text)+2
                text = int(text)

                print(param[:text],end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
