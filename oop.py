# class student:
#     def greet_student():
        # print('Hello student')

# std1 = student
# std2 = student
# std1.name="alan"
# std1.age=18
# print(std1)
# std1.greet_student()
# std2.greet_student()        

#default constructors

# class book:
#     def __init__(self):
#         self.author =""
#         self.title =""

# b1=book()        

#inheritance

#the process of creating a class from another class

#single inheritance

# class staff:
#     def greet(self):
#         print("hello")
# class nonteaching(staff):
#     def introduce(self):
#         print("i am...")

# obj = nonteaching()
# obj.introduce()
# obj.greet()                


#multiple inheritance

# class father:
#     def hobbies(self):
#         print("walking,running")

# class mother:
#     def skills(self):
#         print("singing,dancing") 
# class child(father,mother):
#     def play(self):
#         print("football cricket")

# c1=child()
# c1.hobbies()
# c1.skills()    
# c1.play()          

#multilevel inheritance

# class A:
#     def greet1(self):
#         print("hello")
# class B(A):
#     def greet2(self):
#         print("haii")
# class C(B):
#     def greet3(self):
#         print("hello world")

# c1=C()
# c1.greet1()
# c1.greet2()
# c1.greet3()

#heirarchial inheritance
#polymorphism
#dynamic typing
# class animal:
#     def speak(self):
#         return 'some sound'
    
# class Dog(animal):
#     def speak(self):
#         return 'bow'

# dog = Dog()  
# print(dog.speak())   
# 
# Encapsulation
# public accesible from anywhere
# protected  accessible by the class and the immediate derived
# private  only the class

# class Person:
#     def __init__(self,name,id,phone):
#         self.name = name
#         self.__id = id
#         self._phone = phone
#     def get_id(self):
#         print("id is",self.__id)  

# class Employee(Person):
#     def show_phone(self):
#         print(self._phone) 

# class Developer(Person):
#     def get_phone(self):
#         print(self._phone)   

# p1=Person("Alan",9494858575,84885785885)
# print(p1.name)
# print(p1._phone)        
# p1.get_id()

# dev=Developer("Alan",9494858575,84885785885)
# dev.get_phone()

#abstraction 
#objects cant be created for abstract class

# class Vehicle(ABC):
#      @abstractmethod
#      def start_engine(self):
#           pass
