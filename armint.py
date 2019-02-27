a,b=(int(x) for x in input().split())
for x in range(a,b+1):
  sum=0
  temp=x
  while temp>0:
    digit=temp%10
    sum=sum+pow(digit,3)
    temp=temp//10
  if x==sum:
    print(x)  
  
        
  

