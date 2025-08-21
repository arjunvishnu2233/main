my_list1=["Arun",18,"8"]
print(my_list1[0])

#modify list elements
# my_list1[0]="abhijith"
# print(my_list1)

#inserting new values to the list

#append('value')
# my_list1.append("athira")
# my_list1.append("akhil")
# my_list1.append(36)
# my_list1.append([22,33,35])
# print(my_list1)

#extend(iterables)

# my_list1.extend("ha i")
# print(my_list1)

#insert()

# n=15
# my_list1.insert(5,n)
# print(my_list1)
# print('list before pop :',my_list1)

#pop

# my_list1.pop(1)

#remove (value)

# print('list before removing:',my_list1)

# my_list1.remove('abhijith')
# print('list after removing:',my_list1)

# my_list1.clear()
# print('list after clearing:',my_list1)

# for x in my_list1:
#     print(x)

for i in range(len(my_list1)):
    print(my_list1[1])


    #general methods
    #count(value)
    # print(my_list1.count(12))

    #index
    # print(my_list1.index(12))

    #sort()
    # num=[12,1,57,6,99]
    # num.sort()
    # names=["abhi","karthi","amal","arjun"]
    # names.sort()

    # #reverse()
    # names.reverse()
    # print(names)

    # names_copy=names.copy()
    # names_copy[2]="vishnu"

    # print(names_copy)
    # print(names)

    # list largest
    # list sum
    # list even number count
numbers=[12,7,45,23]
largest_number=max(numbers)
print("largest number:",largest_number)

num1=10
num2=10

sum=num1+num2
print("the sum is:",sum)

numbers=[1,2,3,4,5,6,7,8,9,10]


even_numbers=[num for num in numbers if num % 2 == 0]

print("count of even numbers:",len(even_numbers))

