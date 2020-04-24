#Program to find all the permutations of a string.

def generatePermutation(string,start,end):
    current = 0

    if start == end -1:
        print(string)

    else:

        for current in range(start,end):

            """#Swapping the string by fixing a character"""
            x = list(string)
            temp = x[start]
            x[start] = x[current]
            x[current] = temp

            """#Recursively calling function generatePermutation() for rest of the characters  """

            generatePermutation("".join(x),start+1,end)
            """#Swapping the string by fixing a character"""
            temp = x[start]
            x[start] = x[current]
            x[current] = temp



str = str(input())
n = len(str)
print("All the permutations of the string are: ")
generatePermutation(str,0,n)