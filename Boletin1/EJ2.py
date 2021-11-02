def mayor3(a,b,c):
    if((a > b) and (a > c)):
        return a
    if((b > a) and (b > c)):
        return b
    if((c > a) and (c > b)):
        return c

a = input()
b = input()
c = input()

res= mayor3(a,b,c)
print ("El mayor es ",res)