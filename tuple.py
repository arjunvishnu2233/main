#tuple
#is an ordered collection of data but once created we cannot add new values
#immutable ordered collection of elements
#heterogeneous
#indexed
#allowsduplicatevalues

my_tuple=(12,36,46)
my_tuple2="ligin",45,"jinu"
print(my_tuple2)


#general methods
#count value()
print(my_tuple.count(46))

#index(value)
print(my_tuple.index(36))

numbers=(1,2,3,4,5,6,7,8,9,10)
even=[]
odd=[]

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(odd)        