print("THE PRIME_NUMBER PROGRAM\n")
number= int(input("enter the number\n"))
i=1
co=0
for i in range(1,20):
    if number%i==0:
        co=co+1
    continue
if co>2:
    print("IT IS NOT PRIME NUMBER")
else:
    print("IT IS PRIME NUMBER")
    
    
         
        