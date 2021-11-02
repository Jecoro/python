def suma(a):
    total = 0
    for i in range(len(a)):
        total += a[i] 
    return total
def mult(a):
    total = 1
    for i in range(len(a)):
        total *= a[i]
    return total

print(suma([1,2,3,4]))
print(mult([1,2,3,4]))