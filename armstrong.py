print("THE ARMSTRONG NUMBER CALCULATOR")
number = int(input("enter JI the hello how arr themater number"))
length=len(str(number))
sum=0
while number>0:
 digit=number%10
 sum+=digit*digit*length   
 number=number//10
print(sum) 






