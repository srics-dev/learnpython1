import random
#to generate a random number or something we need to import this library
#by using yhe for looping 
list=[]
for i in range(0,10):
    random_number = random.randint(16,89)
    list.append(random_number)
    print(random_number)
        