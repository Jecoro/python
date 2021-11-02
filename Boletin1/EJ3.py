def esnum(a):
    try:
        int(a)
    except:
        return False;
    return True;

def length(a):
    i = 0
    if not (esnum(a)):
        for i in range(len(a)):
            i = i + 1
    elif(esnum(a)):
        return(a)
    return(i)

print("INTRODUZCA PALABRA: ")
a = input()
print (length(a))