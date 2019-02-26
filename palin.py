a=int(input())
rev_num=0;
ori_num=a
while a>0:
  rem=a%10
  rev_num=rev_num*10+rem
  a=a//10
if rev_num==ori_num:
  print("yes")
else:
  print("no")  
