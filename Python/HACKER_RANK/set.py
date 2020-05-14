'''You have a non-empty set , and you have to execute commands given in

lines.

The commands will be pop, remove and discard. '''

n = int(input())
s = set(map(int,input().split()))
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))