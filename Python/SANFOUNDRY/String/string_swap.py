#Python Program to Form a New String where the First Character and the Last Character have been Exchanged

string = input()

new_string = string[-1:] + string[1:-1] + string[:1]

print(new_string)

