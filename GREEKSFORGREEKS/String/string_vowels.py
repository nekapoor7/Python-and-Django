#Python | Program to accept the strings which contains all vowels

def checkstring(string):

    vowels = set("aeiou")

    s = set({})

    for char in string:
        if char in vowels:
            s.add(char)
        else:
            pass

    if len(s) == len(vowels):
        return ("Accepted")
    else:
        return ("Not Accepted")

if __name__ == "__main__":
    string = input()
    string = string.lower()
    print(checkstring(string))
