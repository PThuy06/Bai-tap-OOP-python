a=int(input('a='))
b=int(input('b='))
a=abs(a)
b=abs(b)
def ucln(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a==b:
        return a
    if a>b:
        return ucln(a-b,b)
    return ucln(a,b-a)
if ucln(a,b):
    print(int(a*b/ucln(a,b)))
