"""count characters at same position in a given string (lower and uppercase characters) as in English alphabet."""

def CountAlphabet(s):
    result = 0
    for i in range(len(s)):
        if ((i == ord(s[i]) - ord('a')) - (i == ord(s[i]) - ord('A'))):
            result += 1
    return result

print(CountAlphabet(input()))