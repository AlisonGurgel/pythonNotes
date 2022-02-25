# functions

""" 
---- DECLARATION DEFINITION ----
def function_name(parameter,[defaultParam=123]):
    statements...
    return value

---- CALL/INVOCATIN ----
function_name(arguments, [defaultArgument=456])  

"""

# builtin functions are language implementation
print("Im builtin")
n = input("also builtin")


# programer declared funtion

def get_marss():
    pass # pass key word are used
         # when you dont know how to inplement
         # the code yet.
 
def get_name():
    name = input("Type your name:")
    return name
user = get_name()
print(f"Welcome, {user.title()}!")

# parameter and default parameter
def get_sum(n1=0, n2=0):
    print(f"{n1} + {n2} = {n1+n2}")
get_sum(3,2)

# default arguments to not change the order
def get_url(prot="https://", dns="google", tld=".com"):
    print(prot+dns+tld)
get_url()
get_url(".com", "youtube", "https://")
get_url(tld=".com",prot="https://",dns="google")

# ---- FUNC EXECUTION CALL STACK? ----

def fa():
    print("satartFa")
    fb()
    print("endFa")

def fb():
    print("startFB")
    print("endFB")
    
fa()
