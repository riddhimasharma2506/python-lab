'''#1 x=int(input("enter first no.:"))
y=int(input("enter second no.:"))
n=int(input("enter any natural no.:"))
i=x+1
for i in range (x+1,y-1):
    if i%n==0:
        print(i)'''
        
'''#2 x=int(input("enter any positive no.:"))
sum=0
while x>0:
    digit=x%10
    sum=sum+digit
    x=x//10
print("sum is:",sum)'''

'''#3 n=int(input("enter any positive no.:"))
if n<0:
    print("invalid input!")
else:
    factorial=1
    i=1
while i<=n:
    factorial=factorial*i
    i=i+1
print("factorial is:",factorial)'''

''' #4 n=int(input("enter any positive no.:"))
original=0
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
if original==reverse:
    print("palindrome number")
else:
    print("invalid number")'''
    
'''#5 n=int(input("enter N:"))
a=0
b=1
i=1
while i<=n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    i=i+1'''
    
'''#6sentence=input("enter any sentence:")
upper=lower=digit=special=0
for i in sentence:
    if i>='A' and i<='Z':
        upper=upper+1
    elif i>'a' and i<='z':
        lower=lower+1
    elif i>='0' and i<='9':
        digit=digit+1
    else:
        special=special+1
print("total upper case letters are:",upper)
print("total lower case letter are:",lower)
print("total digits are:")
print("total special symbols are:")'''

'''#7 n=int(input("enter any number:"))
cnt=0
cnt1=0
k=int(input("enter number:"))
while k!=-999:
    if n%k==0:
        cnt=cnt+1
    else:
        cnt1=cnt1+1
print("total number divisable by n are:",cnt)
print("total number not divisable by n are:",cnt1)'''

'''#8 n=int(input("enter a number:"))
if n<=1:
    print("invalid condition")
else:
    i=2
    prime=true
    
    while i*i<=n:
        if n%i==0:
            prime =False 
            break
        i=i+1 
    if prime:
        print("prime number")
    else:
        print("not a prime number:")'''
        


    


    
    
    