#regularexpression
import re
#match (checking is done at the beginning)match object or none
#re.match('pattern,"data")
# match1=re.match('Hello','Hello,world')
# if match1:
#  print(match1.group())

#search()
# print(re.search('World','hello,World,world'))

#findall()
# print(re.findall('world','hello,world,world'))

#rowstring
# pattern = r'1.2'

#. any character occur once
# print(re.search(r'a.c',"a-pc hbdsjhs"))

#^ starting of a string
# print(re.search(r'^hello','Hello,world'))

#$ ending of a string
# (print(re.search(r'worl d$','hello,worl d')))

#{count},{m,n},{m,}
# print(re.search(r'ca{2,}t','i love cats'))

#is a valid phone number
# phone ='8848932807'
# if (re.search(r'^[6-9]\d{10}',phone)):
#     print(" a valid phone number")
# else:
#     print("provide a valid phone number")

#re.sub

print(re.sub(r'\d+','X','My phone number is 8848932807'))