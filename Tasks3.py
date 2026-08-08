'''
sceret_pin=1234
pin=int(input("Enter the password:"))
while pin!=sceret_pin:
    print("password is wrong")
    pin=int(input("Enter the password:"))
print("password is correct")

   
        

#OTP Verification

OTP=2612
max_attempt=7
current_attempt=0
while current_attempt<max_attempt:
    entered_OTP=input("Enter the OTP:")
    if entered_OTP==OTP:
        print("login succesful")
    else:
        print(" Entered OTP is wrong..")
        current_attempt+=1
else:
    print("Account is Locked,try after 24hrs.....")

secret =123
guess=int(input("enter the password:"))
while guess!=secret:
    if guess<secret:
        print("to low")
        guess=int(input("enter the password:"))
    else:
        print("to High")
        guess=int(input("enter the password:"))
else:
    print("correct guess")


#food order system

food=input("Enter the food:")
count=0
while food!="exit":
    count+=1
    food=input("Enter the food:" )
print("Total number of orders:",count)
'''

secret="python"
current=0
max_attempt=3
while current<max_attempt:
      a=input("enter the secret:")
      if(a==secret):
          print("access agian")
          break
      else:
          remaining=max_attempt-current
          print(f"wrong guess and you have only",remaining)
          current+=1
else:
    print("chances over")



