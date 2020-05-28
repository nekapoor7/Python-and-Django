"""Write a Python function to insert a string in the middle of a string. Go to the editor
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}"""

def insert_string_middle(tag,word):
    return tag[:2]+word+tag[2:4]

print(insert_string_middle('{{}}', 'PHP'))