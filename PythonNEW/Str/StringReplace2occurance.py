"""Write a Python program to get a string from a given string where all occurrences of its
first char have been changed to '$', except the first char itself. Go to the editor
Sample String : 'restart'
Expected Result : 'resta$t'"""
def replacestr(s,source,target,pos):
    s1 = [i for i in range(len(s) - len(source)+1) if s[i:i+len(source)] == source]
    if len(s1) < pos:
        return
    s = list(s)
    s[s1[pos-1]:s1[pos-1]+len(source)] = target
    return ''.join(s)

s = input()
source = input()
target= input()
pos = int(input())
print(replacestr(s,source,target,pos))