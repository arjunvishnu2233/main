my_set={1,2,3,4,5}
print(my_set)

# my_set2= set([12,35,699])
# print(my_set2)

# for x in my_set2:
#     print(x)

    #add
my_set.add((45,47))
my_set.add((45,47))

print(my_set)

#update

my_set.update([45,68,75])
print(my_set)

#deletion

my_set.pop()
print(my_set)

#remove
my_set.remove(45)
print(my_set)

my_set.discard("hello")
my_set.clear()
print(my_set)