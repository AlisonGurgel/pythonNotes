# global
name = "Alison"

def hello1():
    print(name)

hello1()

# local
def hello2():
    n2 = "Gurgel"

hello2()
#print(n2) # error can not acess n2


# local to global
def hello3():
    global n3       # define as global
    n3 = "Decoder"  # than asign a value

hello3()
print(n3)
