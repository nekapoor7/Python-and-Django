mydict = { 'A':'B','B':'D','C':'E','D':'C'}

print(mydict)
print(mydict.get('A'))

def IsReachable(mydict, start, end , path=[]):
    path = path
    if start == end:
        return path
    for node in mydict[start]:
        if node not in path:
            newpath = IsReachable(mydict, node,end,path)
            if newpath:
                return newpath
            return False