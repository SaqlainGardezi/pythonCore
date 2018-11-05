a=13
b="saqlain"
c=34
print (a,b,c)
print(type(a))
x=33.5
y=-54.65
print("Saqlain")
print(type(y))

#complex type
d=3+5j
print(d)
print type(d)

#binary and hexadecimal types
bin=0b10101
hexa=0Xfa18
octal=0o745

""" all have type of int when printed"""

print(bin, " has type ",type(bin))
print(hexa, " has type ", type(hexa))
print(octal , " has type ", type(octal))


#Boolean capital T,F in True,False
boolT=True
boolF=False
print(boolT, " has type ", type(boolT))
print(boolF, ' has type ', type(boolF))

print(5<4)
m=43
n=43
print(m<=n)

#float to int
i=int(x)
print x, " is converted to ", i

#string to float
f=float("22.43")
print(f, " has type ", type (f))

#binary, hexadecimal and octal
deci=23
# it gives error But it should work properly 
''' print(bin(deci)) '''
""" print(bina, " has type ", type(bina)) """
hexa=hex(deci)
octal=oct(deci)
print(hexa, " has type ",type(hexa))
print(octal," has type ", type(octal))

