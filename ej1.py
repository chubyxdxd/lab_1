#first

n=int(input())
ss=""
for i in range(n):
    a=int(input())
    ss=ss+str(a)


#second 
n=int(input())
new_n=0
while n!=0 :
    new_n=new_n*10+n%10
    n=n/10