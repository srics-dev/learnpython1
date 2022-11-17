#This the progran to find the area of the triangle
#the formula to find the area of the triangle is Area of a triangle = (s*(s-a)*(s-b)*(s-c))-1/2
# and s = (a + b + c) / 2 
#to find the area of the triangle we need to know tha value of the a b c
print("Tis the area of the triangle finder")
print("""
      
      
                                          
                                        / 
                                      /    \  
                                    /        \ 
                                  /____________
      
      """)
a=input("enter the value of the one side of the triangle")
b=input("enter the value of the second side of the triangle")
c=input("enter the value of the third side of the triangle")
s=((a+b+c)/2)
area=((s*(s-a)*(s-b)*(s-c))-1/2)
print("AREA of the triangle is",area)