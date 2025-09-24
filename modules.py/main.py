import sample

# sample.greet("alan")

# from sample import *
# greet("roy")

# from functools import reduce
# n=[19,10,5,6]
# result=reduce(lambda x,y:x+y,n)
# print(result)

from functools import reduce
#initializer
n=[19,10,5,6]
result=reduce(lambda x,y:x+y,n,10)
print(result)