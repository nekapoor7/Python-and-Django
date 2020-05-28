"""Write a Python program to wrap a given string into a paragraph of given width. Go to the editor
Sample Output:
Input a string: The quick brown fox.
Input the width of the paragraph: 10
Result:
The quick
brown fox."""
import textwrap
s = input()
N = int(input())
print(textwrap.fill(s,N))