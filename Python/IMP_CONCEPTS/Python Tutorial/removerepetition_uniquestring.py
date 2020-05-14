#python challenge remove repetition​ of letter from string or give me unique letter only

import collections

def removerepeat(string):
    result = collections.Counter(string)
    return result

if __name__ == "__main__":
    my_string = str(input())
    out = removerepeat(my_string)
    print(out)
    for x in out:
     print(x,end='')