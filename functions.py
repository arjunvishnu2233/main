#reusable block of code used for doing a specific task
#built-in functions are aka methods
#syntax
# def function_name():
    #body
    # pass

# def add(x,y):
#     a=x+y
#     return a,x,y

# x=10
# m=45
# n=46
# result = add(m,n)

# print(result)


#lambda functions are called anonymous function

#map()applies functions to all items in a list

my_list = [10,5,11,6]

# sq_num = list(map(lambda x:x**2,my_list))
# print(sq_num)

# def sq(x):
#     return x**2

# my_list2=[]
# for x in my_list:
#     my_list2.append(sq(x))

# print(my_list2)


#filter()

even_num = list(filter(lambda x:x % 2 == 0,my_list))
print(even_num)
# def sq(x):
#     return x**2

# my_list2=[]
# for x in my_list:
#     if x%2 == 0:
#      my_list2.append(x)

# print(my_list2)

# def is_even(x):
#     for x in my_list:
#      if x%2 == 0:
#       return x
#     else:
#        return None 

# my_list2=[]
# for n in my_list:
#      my_list2.append(is_even(n))

# print(my_list2)