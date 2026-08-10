'''
strings --> CaseConversion,searching&finding,string testing methods,replace,space removal

#searching <finding,replacing,joining...
a="Codegnan"

print(len(a))
print(min(a))
print(max(a))

b=a.index('g')
print(b)
c=a.index('n') #it returns only the first occurance
print(c)
d=a.index('n',6) #it returns the next occurance
print(d)
#e=a.index('n',8) #ValueError
#print(e)
f=a.index('t') #ValueError
print(f)
g=a.index('n',1,4)
print(g)


#rindex()--> returns last occurance
b=a.rindex('g')
print(b)
c=a.rindex('n') #here 'n' is occuring at 7th index
print(c)
#d=a.rindex('n',8) #it returns the valueError
#print(d)

#Count() --> returns the number of items object is repeating
print('Codegnan'.count('n'))
print('code'.count('w')) #it returns 0 as we dont have 'w' in 'code'


#find() --> first occurance but it avoid error returns -1 if substring is not found
print('codegnan'.find('r')) #it returns -1 if it is not found

print('codegnan'.find('n'))

print('codegnan'.rfind('n'))


print("Casfgujybk".count('a'))

a="DataAnaylsis"
print(len(a))
for i in a:
    #print(i)
    print(a.count(i),a.index(i))



#Replacing,Splitting,Joining
#Strings are immutable
a='Codegnan'
print(a.replace('g','s'))
print(a)
a=a.replace('g','s')
print(a)
print('ghgygghg#ghujhujhijkjk'.replace('#','  '))
print(a.replace('x','m'))

a='Code saketh python'
b=a.split() #by default if we have space it splits(returns list)
print(b)
print(len(b))
c='code,saketh,python'
d=c.split()
print(d)
e=c.split(',')
print(e)

#join()

a='code'
b='gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('saketh'))
print(' '.join('saketh'))

#string testing methods (boolean)
#isalpha(),isalnum(),isdigit(),isupper(),islower()....

a='Codegnan123'
print(a.isalnum()) #returns true for alphanumeric string else false
b='Codegnan'
print(b.isalnum())
#print(a.isaplha()) #returns True only for alphabets
print(a.isdigit())#returns True only for digit string
print('36578921063'.isdigit())
print('2345'.isnumeric())#this has upper edge(numbers,fraction.romans)
#startswith()--> how its starting

print('codegnan'.startswith('C'))
print('codegnan'.startswith('g',4))
print('codegnan'.endswith('f'))

print('codegnan'.islower()) #returns True for all lowercase
print('COdegnan'.islower()) #returns True for all uppercase
print('Codegnan Python'.istitle())
'''
#Space removal -->strip() (removes leading and trailing spaces)

a='  codegnan  '
print(a.strip())
b=input("Enter the string:").strip().lower()
print(b)














