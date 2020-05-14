def vowels(string):
    count = 0

    vowels = set('aeiouAEIOU')

    for alphabet in string:

        if alphabet in vowels:
            count = count + 1

    print("No. of vowels :", count)

string = str(input("Enter the string"))

vowels(string)