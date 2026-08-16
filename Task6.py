'''
marks=[]
for i in range(3):
    mark=int(input("Enter the marks:"))
    marks.append(mark)
print("original marks:",marks)
marks.insert(0,90)
marks.extend([75,85])
print("After adding 90,75,and 85:",marks)
if 75 in marks:
    marks.remove(75)
    print("75 is removed")
remove_mark=marks.pop()
print("the removed final mark:",remove_mark)
print("The final marks:",marks)
print("Number of marks:",len(marks))


#Number List Analyser

numbers=[20,10,30,20,40,20]
numbers.sort()
print("ascending order:",numbers)
numbers.reverse()
print("descending order:",numbers)
search=int(input("Enter the number:"))
if search in numbers:
           print("Number is found")
           print("Count:",numbers.count(search))
           print("index:",numbers.index(search))
else:
    print("number is not found")
print("Smallest number:",min(numbers))
print("largest numbers:",max(numbers))
print("sum of  numbers:",sum(numbers))


#Even and Odd Number Separator

numbers=[10,15,20,25,30,35]
even=[]
odd=[]
for i in numbers:
    if i %2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:",even)
print("odd numbers:",odd)
print("first three numbers:",numbers[:3])
print("last three numbers:",numbers[-3:])
backup=numbers.copy()
print("backup list:",backup)
numbers.clear()
print("final list:",numbers)


#Unique Name Manager

names=["Asha","Rahul","Asha","John","Rahul"]
names=set(names)
print("Unique Names:",names)
names.add("Meera")
names.update(["Arun","Priya"])
if "John" in names:
    names.remove("John")
names.discard("David")
for name in names:
    print(name)
'''

#Course Student Comparison 

python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"}

both_courses = python_students.union(da_students)

common_students = python_students.intersection(da_students)

only_python = python_students.difference(da_students)

only_one_course = python_students.symmetric_difference(da_students)

is_subset = da_students.issubset(python_students)

is_superset = python_students.issuperset(da_students)

is_disjoint = python_students.isdisjoint(da_students)


print("Students from both courses:")
for student in both_courses:
    print(student)

print("\nStudents learning both courses:")
for student in common_students:
    print(student)

print("\nStudents learning only Python:")
for student in only_python:
    print(student)

print("\nStudents learning only one course:")
for student in only_one_course:
    print(student)

print("\nRelationship Results:")

if is_subset:
    print("DA set is a subset of Python set: True")
else:
    print("DA set is a subset of Python set: False")

if is_superset:
    print("Python set is a superset of DA set: True")
else:
    print("Python set is a superset of DA set: False")

if is_disjoint:
    print("Both sets are disjoint: True")
else:
    print("Both sets are disjoint: False")


