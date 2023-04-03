def nhap():
    l=[]
    n=int(input('nhap n:'))
    print('Nhap',n,'so nguyen:')
    for i in range(1,n+1):
        x=int(input())
        l=l+[x]
    return n,l
def dem(n,l):
    d=0
    for i in l:
        if i>0:
            d=d+1
    return d
def inkq(n,l,d):
        print('Day so da nhap:',end='')
        for i in range (len(l)-1):
           print(l[i],end=',')
        print(l[-1],end='')
        print('\nSo luong so nguyen duong:',d)
n,l=nhap()
d=dem(n,l)
inkq(n,l,d)
