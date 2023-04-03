import re
n=input()
k=True
while k:
    if (len(n)<6 or len(n)>17) :break
    if not re.search('[a-z]',n):break
    if not re.search('[A-Z]',n):break
    if not re.search('[0-9]', n):break
    if not re.search('[$#@]',n):break
    if re.search('\s',n):break
    else:
        print('True')
        k=False
        break

if k:
    print('False')
