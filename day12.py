'''
sequences --> Strings,Lists,Tuples,Set.Frozenset
Mapping -->Dictionary

#sets -->A set is a unqiue collection of objects,Unordered,Mutable,Hashing,Unindexed,unique,Hetrogenous

#set(),{}
#a={} its an empty dictionary
a=set()
print(type(a))
stud_ids={123,345,234,567,234}
print(stud_ids)
print(type(stud_ids))
print(len(stud_ids))
#print(stud_ids[2]) #TypeError

print(234 in stud_ids)
#print(stud_ids*2)#set can't be repeated
#print*stud_id+stud_id) #two sets cannot be merged

#data={1,2,3,4,5,[12,3,4],'saketh'}
#print(data) #no lists inside a set(hashing technique) Lists are Mutable
data={1,2,3,4,5,(12,3,4),'saketh'}
print(data)
print(len(data))
for i in data:
    print(i)
'''
#Method on sets -->add(),update(),remove(),discard(),pop()
names={'sai','saketh','kiran','codegnan'}
print(len(names))
#add will insert an element into set
names.add('python')
print(names)
#names.add('saketh','poll')
#print(names)
names.add(('poll','police'))
print(names)
#names.add({'poll','police'}) #Unhasable
#print(names)

da_names={'mani','akash','sai','sonu'}
print(da_names)
'''
names.update(da_names)
print(names)
print(da_names)
print(len(da_names))
da_names.update(names)
print(len(da_names))
print(len(names))

#names.pop()
#print(names)


#remove(),discard(),pop(),clear()
#remove() 'remove an element from the set(it musst be a member)
da_names.remove('sai')
print(da_names)
#da_names.remove('sai') #keyError
#discard() will remove an element if its present else it ignores
da_names.discard('codegnan')

da_names.pop()
print(da_names)
print(da_names.pop())#removes and return an arbritary element
print(da_names)
da_names.add('Saira')
print(da_names)
da_names.update(['sai','akash'])
print(da_names)
print(len(da_names))
da_names.clear()
print(da_names)
'''

#copy()
d=da_names.copy()
print(d)
d.update(['python','codegnan'])
print(d)
print(da_names)
#d.update('java','html') #it returns the individual element in the given words
#print(d)

#mathematical operations -->union(),intersection(),differance(),symmtric_difference(),issubset(0,issuperset(),isdisjoint()
da_23={12,23,34,45,23,36}
da_24={34,46,47,23}
'''
#event=da_23.union(da_24)
event=da_23|da_24 #| union()
print(event)
print(len(event))
#common=da_23.intersection(da_24)
common=da_23&(da_24) #& intersection()
print(common)
print(len(common))

common=da_23.intersection_update(da_24)
print(common) #it returns None
print(da_23) #common elements are finally stored

print(da_23)
print(da_24)
#diff=da_23.difference(da_24)
#print(diff)
#f=da_23-da_24 #- differnece()
#print(f)
#symm=da_23.symmetric_difference(da_24)
#print(symm)
#h=da_23^da_24 #^ symmetric()
#print(h)
#issubset() --> checks for all ellements to be present in other set

da_24.remove(46)
da_24.remove(47)
print(da_23.issubset(da_24))
print(da_23.issuperset(da_24))

#isdisjoint() returns false for sets having common elements
print(da_23.isdisjoint(da_24))
'''
#Length of unique student ids in a class,whee user can enter first input he should be giving number of student_id,he will enter student-ids

n=int(input())
student_ids=input().split()
#print(student_ids)
result=set(student_ids)
print(len(result))


