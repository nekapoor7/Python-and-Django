"""Write a Python function to reverses a string if it's length is a multiple of 4."""

def Reverse(words):
    if len(words) % 4 == 0:
        return ''.join(reversed(words))
    return words

if __name__ == "__main__":
    words = input()
    print(Reverse(words))