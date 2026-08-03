'''
control,statements --> Contrl of Flow of Exceution of the program
                   --> Conditional statements -->.if,elif,else...
                   --> Repetition Statements(Loops) -->for,while(for with else) (while with else)
                   -->Jumping statements-->break,continue,pass
'''
#Loops --> Loops are helpful for repitions(Automative tasks)
#for keywprd will be helpful to iterate over a sequence / range
#Syntax for(for keyword):
'''
for<temp_var> in sequence/range:
    statement(s)....
    ............


#range(start,stop,step)
#by default range picks 0 as start value
for i in range(10):
    print(i)
#In above case we got 10 iterations
for i in range(1,10): #range(stop) -->default 0 ends at stop-1
    if i > 5:
        print(f'Value of i is -->{i}')

#Now i want  to get only even numbers with above conditio
for i in range(1,10):
    if i < 5 and i%2==0:
        print(f'final value of i is--->{i}')


#range(start,stop,step)-->here step--->interval..
for i in range(-10,0,1):
    print(i)
    print("Done")


#[] -->we generally Lists
names=['devi','sneha','jyothi']
print(len(names)) #len(obj) --> returns the number of items in a container
for name in names:
    #print(name)
    #print(f'student name is{name}')
    if name =="sneha":
        print(f"student name is {name}")


#calculate the sum of first 10 numbers
#first understand your input -->range(11) -->10 numbers
#second understand your output -->sum(number)
#third we need to map the logic

result=0 #target variable
for i in range(11):
    result=result+i #result +=i
    print(f'now the result is{result}')
print(f'sum of 10 numbers is {result}')
#sum of first 10 even numbers

result=0
for i in range(21):
    if i%2==0:
        result=result+i
        print(f'sum of 10 even numbers is {result}')
'''
#understand the loops usage with Fitness streak example
#work_out -->1,work_out_missed -->0

work_log=[0,1,1,1,0,1,0]
#result variable --> longest_streak
longest_streak =0 #target variable
current_streak=0
for day in work_log:
    if day==1:
        #print(day)
        current_streak=current_streak+1
        if current_streak > longest_streak:
            longest_streak=current_streak
    else:
        current_streak=0
print(longest_streak)
