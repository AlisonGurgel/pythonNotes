
def get_name(first, middle, last):
    print(f"name: ",first,middle,last)


# positional arguments the order metters
print("positional")
get_name("Alison", "Gurgel", "Decoder")
get_name("Gurgel", "Decoder", "Alison")

 
# keyword arguments
print("keyword")
get_name(middle="Gurgel", last="Decoder", first="Alison")
    

try:
    get_name() 
except TypeError:
    print("we need 3 positional arguments")
    print("(first, middle, last)")
else:
    print("Ok")
    
# default parameters

def addNumberMultiply(n1=0, n2=0, n3=0):
    print((n1+n2)*n3)

# positional arguments the order metters
addNumberMultiply(4,4,2)
addNumberMultiply(2,4,4)

# keyword arguments
addNumberMultiply(n1=4, n2=4, n3=2)
addNumberMultiply(n3=2, n1=4, n2=4)

