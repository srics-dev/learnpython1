print("simple interest progrm")
money=int(input("enter the money"))
percent=float(input("enter the percentage"))
year=int(input("enter the year"))
simple=(money*percent*year)/100
print("the simple interest",simple)
total=money+simple
print("total amount",total)