
'''x1= int(input("enter the points of cirlce x1: "))
x2 = int(input("enter the points of cirlce x2: "))
y1 = int(input("enter the points of cirlce y1: "))
y2 = int(input("enter the points of cirlce y2: "))
radius = int(input("enter the radius of circle:"))
formula = (x2-x1)(x2-x1) + (y2-y1)*(y2-y1) 
distance = formula**0.5
if distance < radius :
    print("point is inside the circle :", distance)
elif distance == radius :
    print("point is on the cirlce=",distance )
else : 
    print("point is outside the circle=", distance)'''
    
    
'''s = int(input("enter the side of pentagon:")) 
area = (5*s**2)/(4*0.7265)
print("area of pentagon", area)''' 


'''x = int(input("enter the angle 1 : "))
y = int(input("enter the angle 2: "))
z = int(input("enter the angle 3: "))
if x + y+ z = 180 :
    print("they can form triangle")
    if y>90 :
        print("obtuse angled triangle")
    elif y == 90 :
        print("right angled triangle")
    elif y < 90:
        print("acute angled triangle")
else : 
    print("they cannot form triangle")'''
    
    
'''n = int(input("enter 4-digit number: "))
d1 = n//1000
d2 = (n%100)//100
d3 = n%1000%100//10
d4 = n%10
sum1 = d1 + d2
sum2 = d3 + d4  
print("sum1",sum1)
print("sum2", sum2)'''


'''n = int(input("enter the 5-digit number: "))
a = n//10000
b = (n%1000)/1000
c = n%10000%1000/100 
d = n%10000%1000/10
e = n%100 
if a>b and a>c and a>d and a>e:
    print("a is largest")
elif b>a and b>c and b>d and b>e:
    print("b is largest")
elif c>b and c>a and c>d and c>e:
    print('c is the largest ')
elif d>b and d>c and d>a and d>e:
    print("d is the largest ")
else :
    print('e is the largest ')'''
    
  
'''a = int(input("enter first variable:"))
b = int(input("enter second variable: "))
c = int(input("enter third variable: "))
a = a+b+c
b= a-b-c 
c=a-b-c
a=a-b-c
print("after swapping:",a,b,c)''' 


'''n = int(input("enter 3 digit number: "))
d1 = n//100
d2 = (n%100)/100 
d3 = n%10
if n//(d1+d2+d3) == 0 :
    print("it is harshad number")
else: 
    print("it is not harshad number")'''
    


'''v = int(input("enter the volume of water initialy: "))    
n =int(input("enter the number of days: "))
water = v*(0.95**n)+200*(1-0.95**n)
if v<0:
    print('invalid input')
else:
    print("quantity of water=", water) '''
    
'''#a1x+b1y=c1 and a2x+b2y=c2    
a1 = int(input("enter the coefficient a1: "))
b1 = int(input("enter the coefficient b1: "))
c1 = int(input("enter the coefficient c1: "))
a2 = int(input("enter the coefficient a2: "))
b2 = int(input("enter the coefficient b2: "))
c2 = int(input("enter the coefficient c2: "))
x = -b1/a1 
y = -a2 / b2 
if a1 == -a2 :
    print("y")
elif b1 == -b2 :
    print("x")
else: 
    print("parallel lines")''' 


