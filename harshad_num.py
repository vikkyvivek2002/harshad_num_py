x = int(input("enter a number"))
y,sum=x,0
while(y>0):
    rem=y%10
    y=y//10
    sum = sum +rem
    
if(x%sum == 0):
    print("harshad number")
else:
    print("not a harshad number")
