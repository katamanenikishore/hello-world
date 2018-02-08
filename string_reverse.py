__author__ = 'kkataman'

inp = raw_input("enter a string:")
list1 = []
for item in reversed(inp.split(' ')):
    list1.append(item)
    
print ' '.join(list1)
