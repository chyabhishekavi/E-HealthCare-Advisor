import csv
f= open("C:\\Users\\AMARJEET ANAND\\Music\\New folder (3)\\flagged\\log.csv","r")
p=[]

for row in f:
    p.append(row)

ctr=0
k=0
m=-1
x=[]
for i in p:
    if ctr==0:
        ctr=1
    else:
        k=0
        for j in i:
            if j==',':
                break;
            else:
                k=k+1
        x.append(k)
print(x)
# ctr=0
# k=input("enter k")
# for i in p:
#     if ctr==0:
#         ctr=1
#     else:    
#         if p[ctr][0:x]==k:
#             for j in i:
#                 print(j,end="")
#             print()    
#             ctr=ctr+1
#         else:
#             ctr=ctr+1    




