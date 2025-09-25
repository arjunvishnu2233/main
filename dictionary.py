#mutable
#ordered
#unindexed
#key-value pairs
#once a key is created we cannot change it
#unique keys
#heterogeneous
#keys are represented in string 

my_dict={
    "name":"example",
    "rno":0
}

students={"name":"arun","rno":4,"class":10,"hobbies":["reading","coding","dancing"]}

print(students["hobbies"])

#keys
# print(students)

# for x in students.keys():
#     print(x)
# #values
# print(students.values())

# for y in students.values():
#     print(y)
# #items

# print(students.items())

# for x,y in students.items():
#     print(x,':',y)

#students.update(rno=6)

#students.pop("class")

#students.popitem()

#studentsvalues=students.values()
#students["name"]=abhijith"

#students["phone"]=8086564409
#students.update({"name":"akhil"})

#del students["hobbies"]

#students.clear()
print(students)

students= [

    {"name":"akhil","age":15,"rno":1,"marks":[45,60,80]},
    {"name":"arun","age":14,"rno":2,"marks":[71,90,47]},
    {"name":"aji","age":15,"rno":3,"marks":[96,69,30]},
    {"name":"akhi","age":13,"rno":4,"marks":[45,74,80]},
]

print("names:")

# for student in students:
#     #print(student["name"])
#     student_name=student["name"]
#     marks=student["marks"]
#     average_marks=sum(marks)/len(marks)
#     print("average marks for {student_name}:{average_marks}")
    
