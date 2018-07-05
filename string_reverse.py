__author__ = 'kkataman'

inp = raw_input("enter a string:")
list1 = [] #to hold reversed string
for item in reversed(inp.split(' ')):
    list1.append(item)
    
print ' '.join(list1)
print 'test'