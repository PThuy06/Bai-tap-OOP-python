n=int(input())
s = n*[0]
def tt1(s,i):
   for j in range(i,n):
      s[j] = 0
def tt2(x):
   d = ''
   for i in x:
      d=d+ str(i)
   return d


while True:
   print(tt2(s))
   i = n - 1
   while (i > -1) and s[i] == 1:
      i = i - 1
   s[i] = 1
   tt1(s,i+1)
   if i == -1:
      break
