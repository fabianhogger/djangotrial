x = int(input())
y = int(input())
z = int(input())
n = int(input())
x=[i for i in range(0,x+1)]
y=[j for j in range(0,y+1)]
z=[z for z in range(0,z+1)]
res=[[i,j,k]  for i in x for j in y for k in z  if(i+j+k)!=n ]
print(res)
