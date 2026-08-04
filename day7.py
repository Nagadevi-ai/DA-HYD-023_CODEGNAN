'''
usage

#for with else...


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
            print(longest_streak)
            #break
    else:
        current_streak=0 #streak break
else:
    print(f'longest streak is {longest streak}')

#In this case when the entire loop execution is done we get result of
#else block

#for else with Notificatins scenario

notifications=[1,0,1,0,]
for notification in notifications:
    if notification == 1:
        print('unread notification')
        break

else:
    print('All caught up')

#try to take notifications from user --> list of integers

notifications=list(map(int,input("Enter the values--> 0 or 1:").split(',')))
for notification in notifications:
    if notification == 1:
        print('unread notification')
        break

else:
    print('All caught up')


#while -->it telies on condition, it will be completely executed until the condition is satisifed

Syntax while:

while<condition>:
    statement(s)...
    .........
    .........


while True:
    print('yes')

#It runs an infinite loop we need to press ctrl+c(keyboard interrupt)

i=0
while i<=10:
    print(i)
    i=i+1 #counter

i=10
while i>=1:
    print(i)
    i=i-1 #decrement i-=1
'''
#banking scaenario -->PIN authentication if more than 3 attempts
#Account locked....
pin="2612"
max_attempts=3
current_attempt=0
while current_attempt < max_attempts:
    entered_pin=input("enter the ATM pin:")
    if entered_pin==pin:
        print("Login successful")
        break
        #continue # it holds for this condition and skips to the next part
    else:
        print("Entered PIN is wrong...try again carefully")
        current_attempt +=1
else:
    print("Account Locked,try after 24 hours...")


    
    
 

    
