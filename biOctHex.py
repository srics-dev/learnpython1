def decimal_to_binary(x):
    decimal1=x
    print("in binary",bin(decimal1))
def decimal_to_oct(x):
    decimal1=x
    print("in oct",oct(decimal1))
def decimal_to_hex(x):
    decimal1=x
    print("in hex",hex(decimal1))
decimal=int(input("enter the decimal number: "))
decimal_to_binary(decimal)
decimal_to_oct(decimal)
decimal_to_hex(decimal)        