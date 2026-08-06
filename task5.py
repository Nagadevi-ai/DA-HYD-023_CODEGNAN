'''
#task 1

product= list(map(int,input("Enter the price:").split(',')))
result=0
for i in product:
         result=result+i
print(result)


#task 2

password = input( "Enter the password:")
upper=lower=special=digit=0
for ch in password:
    if 'A'<=ch<='Z':
        upper+=1
    elif 'a'<=ch<='z':
        lower+=1
    elif '0'<=ch<='9':
        digit+=1
else:
    special+=1
    print("upper:",upper)
    print("lower:",lower)
    print("digit:",digit)
    print("special:",special)


#task 3

email=input().split()
for mail in email:
    print(mail.split("@")[1])


'''
#task4

movies=["salaar","bahubali","KGF"]
print("Move List:")
for movie in movies:
    print(movie)
    

























