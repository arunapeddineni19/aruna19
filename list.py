a,c=(int(x)for x in input().split())
l=[]
sum=0
for i in range(1,a+1):
  l.append(i)
print(*l)
for i in range(1,c+1):
  sum=sum+i
print(sum)  

