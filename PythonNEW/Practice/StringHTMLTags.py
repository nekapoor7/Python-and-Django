"""Write a Python function to create the HTML string with tags around the word(s). Go to the editor
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'"""

def add_tags(tag,word):
    return '<%s>%s</%s>'%(tag,word,tag)

print(add_tags(input(),input()))