'''
sequences --> Strings,Lists,Tuples,Sets
Mapping -->Dictionary



#Lists-->Collection of heterogenous elements(items)
#List -->Indexed,ordered,Mutable,Heterogenous,We use [] to store the data

marks=[34,39,21,36]
print(marks)
print(len(marks))
print(type(marks))

#operatins : Indexing,Slicing,Striding,Membership,Merging,Reptition


#Nested Lists-->A list inside another list

names=['Codegnan',25,4.6,[45,35,25,65],'DA23',34]
print(len(names))
print(names[0])
print(names[-3])
print(names[3])

print(names[0][:4])
print(names[0][4:])
print(names[0][0::2])
#names[0]=names[0][::-1]
print(names)

print(names[3])
print(names[3][2])
print(len(names[3]))

#Indexing,Slicing -->Mutable
names[2]='python'
print(names)
#By indexing if we change the elements of collection will remain same
#names[4]=['Codegnan','PFS','DA','AAA','DS']
print(names)
print(len(names))
print(names[4][0][4:])
names[2:4]='Abhiram','Sairam','saketh','sai'
print(names)
#In slicing whatever elements u pass as per the logic length keeps on increases
names[3:6:2]=['python','java']
print(names)
'''

#Create a nested list with a strings,lists and work on indexing,Slicing,Striding,Added advantade if u could add string funstions also

#Lists Function --> append(),insert(),extend(),pop(),remove(),clear(),index(),count(),copy(),sort(),reverse()

names=['codegnan','saketh']
#append --> inserts single element to the end of the list
names.append('data')
print(names)
#names.append('Analysis','agents')#TypeError
#print(names)
names.append(['Analysis','agents'])
print(names)
#append() will always increment the length of list by 1
print(names[3])
#names[3].append('chatgpt')
print(names)

#extend() --> inserts multiple elemnts to the end of list

#names.extend('analysis') #string will be splitted
print(names)
#names.extend(['analysis'])
print(names)
#names.extend([45,76,78,98])
print(names)
#name.extend(35,45) TypeError
#print(names)

#insert(index,object)-->inserts given object before index
names.insert(1,'python')
print(names)
names.insert(0,'java')
print(names)
#names.insert([1:4],['a','b']) #SyntaxError
#print(names)
names.insert(-1,'AAA')
print(names)

#pop(),remove(),clear()
#pop() by default last,else given index
names.pop()
print(names)
names.pop(2)
print(names)

#remove() we can remove a specific value
names.extend([23,14,15])
print(names)

names.remove(14)
print(names)

del names[1:3]#del keyword will apply permannnet changes
print(names)
names.clear() #clear() will remove alll elements and returns empty list
print(names)

#data=['codegnan','saketh','python','java'] #input
#output should be follows
'''
0:codegnan
1:saketh
2:python
3:java
'''
