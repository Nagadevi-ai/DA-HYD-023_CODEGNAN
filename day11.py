'''
Lists,Tuples..

#List -->Mutable,Ordered,Heterogenous

#index(),count(),copy(),sort(),reverse()

details=['codegnan',7,2018,'Hyderabad']
print(len(details))
print(details.index(7))
print(details.index('codegnan'))
details.extend([7,21,45,21])
print(details.index(21))#it returns first occurance
print(details.index(21,6))
#print(details.index('python')) #ValueError
print(details.count(21))
print(details.count('python')) # it returns 0 as we dont have it
'''

#data=['codegnan','saketh','python','java'] #input
#output should be follows
'''
0:codegnan
1:saketh
2:python
3:java

for obj in data:
    print(data.index(obj),':',obj)


for obj in range(len(data)):
    print(obj,':',data[obj])
   

#copy() -->Shallow copy of the given collection

new=data.copy()
print(new)
print(type(new))
print(len(data))

new[2]='Agentic Ai'
print(new)
print(data)

data.append('saketh')
print(data)
print(new)

print(new[3])

data=[1,4,5,[21,34,45],23]
print(data)
new=data.copy()
print(new)

new[3][2]='Agents' #whenever we make change in nested list original will also be effected
print(new)
print(data)

new[1]='python'
print(new)
print(data)



marks=[14,24,-45,27,35]
#print(marks)
#marks.sort()
print(marks)
marks.sort(reverse=True) #returns it Descending order...
print(marks)
print(marks[3])
print(marks.index(24))
marks.insert(2,'code')
#marks.sort()
#reverse()-->returns in reverse order
marks.reverse
print(marks)
print(marks[::-1])
print(marks)


#type(),len(),max(),min(),print()

print(sorted('codegnan')) #returns List in ascending order
#print(sorted(['code',23,45,45]))#raises error


#Tuples --> Tuples are Indexed,Ordered,Heterogenous,immutable collection
#dimensions,Coordinates,database records,we prefer() for tuple notation

a=()
print(type(a))
print(len(a))

dim=1.5,2.5
print(dim)
print(type(dim))
print(len(dim))
'''
#operations -->Indexing,Slicing,Stridind,Membership,Merging,REpition

courses=('PFS','JFS',('DA','DS'),'AgenticAI',[100,6,6])

'''
print(courses)
print(len(courses)) 
print(courses[-2][-2:])
#courses[2]=23 Tuple are immutable
courses[-1].append('codegnan') #we can make any modifications inside list
print(courses)

#create a nested tuple as above and work on slicing striding and list function
print('PFS'in courses) #Membership
d=courses*2
print(d)
e=courses +(2,3,4,5) #merging
print(e)

print(courses.index('AgenticAI'))
print(courses.count('Agents'))

#print(courses.sort()) #AttributeError -->sort() is in Lists not in Tuples

print(sorted(courses[-1]))
#print(sorted(courses)) #as we have mixed type

#TypeCasting
d=tuple(sorted((23,12,3,4,5)))
print(d)


#accept group of integers space separted
a,b=map(int,input("Enter the value:").split(','))
print(a,b)

print('9+4')
print(eval('9+4'))
'''
a=eval(input("Enter a list:")) #in this case u can exactly enter data as list
print(a)
print(type(a))

#Task:Take a user input as string,do this in two ways
'''
1)give the count of each repeating charcter
Test case 1: programming

r is repeating 2 times
g is repeating 2 times
m is repeating 2 times


2)
r is repeating 2 times
index=[1,4]
g is repeating 2 times
index=[3,10]
m is repeating 2 times
index=[3,10]
'''






















