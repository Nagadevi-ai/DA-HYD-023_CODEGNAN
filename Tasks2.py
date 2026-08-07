'''
#write a python program to calculate the innings of batsman and count the boundaries ,dot ball.total score.

runs=[4,6,1,0,2,4,0,6]
total_score=0
total_boundaries=0
total_dotballs=0
for run in runs:
    total_score=total_score+run
    if run == 0:
        total_dotballs=total_dotballs+1
    if run==4 or run==6:
        total_boundaries= total_boundaries+1
print("Total_boundaries:",total_boundaries)
print("Total_score:",total_score)
print("Total_dotballs:", total_dotballs)


# Pattern Analyzer

password=1234
max_attempt=5
current_attempt=0
while current_attempt<max_attempt:
    entered_password=input("Enter password:"))
    if entered_password==password:
        print("phone unlocked")
    else:
        print("enter password is wrong")
        current_attempt+=1

else:
    print("The Phone is Locked,try after 30 seconds...")


#ATM PIN

pin=2612
max_attempt=3
current_attempt=0
while current_attempt<max_attempt:
    entered_pin=input("Enter the Pin:")
    if entered_pin==pin:
        print("login succesful")
    else:
        print(" Entered PIN is wrong..")
        current_attempt+=1
else:
    print("Account is Locked,try after 24hrs.....")
        
'''  



                                





