print("-- variables --") 

name   = "Alison"
age    = 17
weight = 100.50
alive  = True

print(f"name:   {name}")
print(f"age:    {age}")
print(f"weight: {weight}")
print(f"alive:  {alive}")

print(" -- variable types --".upper())
print(f"name:   {type(name)}")
print(f"age:    {type(age)}")
print(f"weight: {type(weight)}")
print(f"alive   {type(alive)}\n")

# data structures
print("-- datastructures --".upper())
fruits = ["banana", "apple", "orange"]
animal = ("zebra", "giraff", "bat")
number = {1,2,3,4,5,6,7,8,9}
person = {name: "john", age: 17}

print(f"fruits: {fruits}")
print(f"animal: {animal}")
print(f"number: {number}")
print(f"person: {person}\n")

print(f"fruits {type(fruits)}")
print(f"animal {type(animal)}")
print(f"number {type(number)}")
print(f"person {type(person)}")
print("\n")

# ------------
print("builtin functions".upper())
print(f"type():  {type(type)}")
print(f"print(): {type(print)}")
print(f"max():   {type(max)}")
print(f"min():   {type(min)}")
print(f"ord():   {type(ord)}")
print(f"chr():   {type(chr)}")

# variables are class/obj
car = str()
cpu = int()
kil = float() 
wor = bool()

arr = list()
tup = tuple()
se7 = set()
dik = dict()

boo = None

print(car, type(car))
print(cpu, type(cpu))
print(kil, type(kil))
print(wor, type(wor))

print(arr, type(arr))
print(tup, type(tup))
print(se7, type(se7))
print(dik, type(dik))

print(boo, type(boo))

