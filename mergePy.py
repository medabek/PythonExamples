def merge_the_tools(string, divider):    
    l=len(string)//divider
    for i in range(l):
        substr=''
        for c in string[i*divider:i*divider+divider]:
            if c not in substr: 
                substr+=c
        print (substr)
print(merge_the_tools("AABCAAADA", 3))
