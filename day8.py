'''
Sequences --> strings,lists,sets,tuples,mapping(dict)

#Strings --> Group of characters,we use single or double or triple quotes
#for representation of strings...
#Strings are immutable, ordered,Indexed Collection

name="Codegnan"
print(name)
print(type(name))
print(len(name)) #len --> returns the number of items in container

#index() -->fetch the object (postion) starts at 0and ends at len(obj)
#we use [] representation
print(name[0])
#print(name[25]) #IndexError -->as its out of range

#Negative Indexing --> -1 to len(obj)
print(name[-1]) #it returns last character
print(name[-5])
#print(name[-33]) # IndexError --> as its out of range

#Slicing -->we can access group of characters(objects)
#we use[start:end] #start default -->0,start is included,end is exculded

print(name[:]) # it returns entire string
print(name[0:]) # it returns entire string
print(name[:4]) #starts at 0th index before 4th index
print(name[1:5]) # starts at 1th index before 5th index
print(name[-4:-7])

name="python"
print(name[7:3]) #returns empty as string are immutable
#slilcing is applicable from lower index  to higher index
print(name[:45])#returns till end of the string
print(name[45:]) #return the empty

#print 'on' from above string
print(name[1:5])
print(name[4:])
print(name[-2:])

print(name[1:-2])
print(name[2:-6])
#observe +ve,+ve,-ve,&+ve,-ve all possibilites

#striding -->[start:end:step]

course="DataAnalysis"
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

#task:workout with all possiblites of slicing annd striding on a  example

name='codegnan'
#name[3]='w' #strings are immutable
#oprations on strings-->Indexing,concatenation,Reptition
print(name * 3)
print('*' *25)

#Concatenation -> combining stings

data = 'Nagadevi'+ '  '+ 'python'+ '  ' +'data'
print(data)
print('123' * 5)
print('code' in 'codegnan')

for i in 'codegnan':
    print(i,':')
#in the above case we get every character line by line

for i in 'codegnan':
    print(i,end=' ')



name='Codegnan'
#Built-in functions -->length(),.min(),max(),sorted()
print(len(name))
print(min(name)) #alphabetical order ASCII ordering
print(ord('A'))
print(ord('a'))
print(max(name))
print(chr(97))
print(sorted(name)) #returns a list by sorting all elements

'''

#Methods on strings -->Case-Conversion,Finding/Searching...
name='codegnan data'
#Case-Conversion --> upper(),lower(),title(),capitalize()
a=name.upper()
print(a)
b=name.lower()
print(b)
#Capitalize()->converts first letter to uppercase
c=name.capitalize()
print(c)
d=name.title() #converts every work first letter to uppercase
print(d)

#Task:A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#use loops and strings to return A-Z
