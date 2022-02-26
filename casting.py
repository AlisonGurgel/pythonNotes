x = 123 # int
print(x, type(x))

x = str(x) # int to string
print(x, type(x))

x = bool(x) # string to boolean
print(x, type(x))

x = int(x) # boolean to int
print(x, type(x))


#x = 123  int cant cast to itarables
x = "123" # string to list
x = list(x)
print(x, type(x))

x = tuple(x) # list to tuple
print(x, type(x))

x = set(x) # tuple to set
print(x, type(x))

""" error
x = "a:1,b:2"
x = dict(x)
print(x, type(x))
"""

