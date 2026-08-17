'''
Mapping -->Dictionary --> Collection of keyvalue pairs used to store realted to data
JSON,APIs,database records

dict() -->data={} -->{key:value}
Dictioonary is Mutable,Indexed through keys,ordered,Heterogenous,keys must be Unique(int,strings,float values...)
'''
details={}
print(type(details))
details={'Id':'CGH4021','Name':'Nagadevi',
         'Gender':'female','Age':22,
         'Batch':'DA23','place':'HYd'}
print(details)
print(len(details))

#Access the data from dictionary
#details[0] #KeyError
'''
print(details.keys()) #it returns keys from the dictionary
print(details['Id'],details['Name'])

#if key name is not matching/invalid
#print(details['marks']) #KeyError as marks is not present
details['marks']=[]
print(details)
print(type(details['marks']))

details['marks'].append(20)
print(details)

details['marks'].extend([30,45,65,78,75])
print(details)

#Create a key value pair of Practice Session
details['Ps']=('Tuesday,thursday,saturaday')
print(details)

#Accessing 3rd day marks of student
print(details['marks'][2])
#Accessing 2nd day of practice Session
print(details['Ps'][1])
details['MI']=('Monday','Wednesday','Friday')

#operations-->mutable,indexing,through keys,membership

print('Wednesday' in details)
print('MI' in details) #returns True

for i in details:
    print(i) #returns keys one by one

for i in details.keys():
    print(f'Key={i}')
    print(f'Value ={details[i]}')
#key() --> returns keys from the dictionary

for i  in details.values(): #returns values of dictionary
    print(i)

for i in details.items(): #returns a key-value pair in tuple
    print(i)
    
for key,value in details.items():
    print(f'key is {key}')
    print(f'value is{value}')


#update()
details.update({'marks':[],'PS':('tue','thu','sat')})
print(details)
details['marks'].extend([25,56,78])
print(details)

marks=list(map(int,input("Enter the marks:").split(',')))
print(marks)
details['marks'].extend(marks)
print(details)

'''
print(details.keys())
print(details.get('Name'))
print(details.get('Branch')) #it returns None as we dont have branch as key
details.setdefault('Branch') # if key is not present it inserts into dict
print(details)
details['Branch']='CSE'
print(details)

print(details.setdefault('Name'))
print(details.keys())

print(details.pop('Branch')) #we need to mention key
print(details.keys())

print(details.popitem()) #Removes and return a key,value pair as a 2-tuple
print(details.popitem())

del details['Id']
print(details.keys())

details.clear() #remova all elements from 0
print(details)

#fromkeys()
data=['saketh','sai','data']
print(dict.fromkeys(data)) # creates a dict but values set to None
b=dict.fromkeys(data)
print(b)
b['saketh']=31
print(b)
c=dict.fromkeys(['CGH1234','CGH2345'],['code','gnan'])
print(c)


#Task: Create a dictionary with your personal details,simliar to your codegnan profile
