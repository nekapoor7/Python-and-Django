""" Break

Break statement is used to jump out of loop to process the next statement in the program.

Continue statement is used in a loop to go back to the beginning of the loop.

Pass statement is used to do nothing. It can be used inside a loop or if statement to represent no operation.
pass is useful when we need statement syntactically correct but we do not want to do any operation."""

for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)

