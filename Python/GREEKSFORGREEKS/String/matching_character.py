#Count the Number of matching characters in a pair of string

def matchchar(str1,str2):
    count = 0
    setA = set(str1)
    setB = set(str2)

    matched_charatcters = setA.intersection(setB)
    print(matched_charatcters)
    for i in matched_charatcters:
        count += 1
    return count

if __name__ == "__main__":
    string1 = str(input())
    string2 = str(input())
    print(matchchar(string1,string2))
