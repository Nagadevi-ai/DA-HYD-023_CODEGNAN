'''
course="Nagadevi"
print(len(course))
print(course[:4])
print(course[4:])
print(course[-3:])

print(course[::1]) #returns all characters
print(course[::2]) #includes start to end skipping 1 charcater
print(course[1:6:3])#[1:6] --> ataAn -->[1:6:3]-->aA
print(course[2::3]) #returns tnys

print(course[::-1]) #it returns the reverse string
print(course[::-2])

print(course[:]) # it returns entire string
print(course[0:]) # it returns entire string
print(course[:4]) 
print(course[1:5]) 
print(course[-4:-7])
'''

#Task:A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#use loops and strings to return A-Z

for i in range(65,91):
    print(chr(i),end=' ')
