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

# print(re.sub(r'\d+','X','My phone number is 8848932807'))

#re.split
# re.split('pattern','string')

#\escape character
# date=r'20\12\2025'
# print(re.search(r'\\',date)) 

#capturing groups

# msg='my birthday is 20-12-2025'

# pattern = r'(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{4})'

# match=re.search(pattern,msg)

# print(f'date:{match.group('day')}')
# print(f'month:{match.group('month')}')
# print(f'year:{match.group('year')}')

# print(f'date:{match.group(1)}')
# print(f'month:{match.group(2)}')
# print(f'year:{match.group(3)}')

1-31
1-12