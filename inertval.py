lower,upper=(int(x)for x in input().split())
l=[]
for num in range(lower,upper):
  if num>1:
    for x in range(2,num):
      if num%x==0:
        break
    else:
      l.append(num)
print(*l)        
