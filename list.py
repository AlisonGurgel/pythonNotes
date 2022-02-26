# how to create a list
user_names = ["ana", "bely", "cowby"]
print(user_names, type(user_names))

user_names = list(["aren", "berdy", "casy"])
print(user_names, type(user_names))

# list len, the sum of of all items
# an item is coma separated
print(len(user_names))

# list item index
#    0        1        2
# ["aren", "berdy", "casy"]
#   -3       -2       -1
print(user_names[0])
print(user_names[-3])

# list[star : end : step]
print(user_names[0::2])   # aren casy
print(user_names[-1::-2]) # casy aren
