#Program to find the longest repeating sequence in a string.

def longest_common_prefix(string,t):
    n = min(len(string),len(t))
    for i in range(0,n):
        if string[i] != t[i]:
            return string[0:i]
        else:
            return string[0:n]


string = str(input())
length_lrs = ""
n = len(string)

for i in range(0,n):
    for j in range(i+1,n):
        """ #Checks for the largest common factors in every substring  """
        x = longest_common_prefix(string[i:n],string[j:n])
        """#If the current prefix is greater than previous one   
        #then it takes the current one as longest repeating sequence  """

        if len(x) > len(length_lrs):
            x = length_lrs
print("Longest repeating sequence: "+length_lrs);



