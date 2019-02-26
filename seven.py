a,b=(int(x)for x in input().split()) 
l=[]  
for x in range(a+1,b+1):
  if x%2==0:
     l.append(x)  
print(*l)  

   
