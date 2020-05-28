"""Write a Python program that accepts a comma separated sequence of words as input and prints the unique words
in sorted form (alphanumerically). Go to the editor
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red"""

items = input()
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))