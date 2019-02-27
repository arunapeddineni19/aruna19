a=int(input())
temp=a
sum=0
while temp>0:
  digit=temp%10
  sum=sum+digit ** 3
  temp=temp//10
if a==sum:
  print("yes") 
else:
  print("no")   

