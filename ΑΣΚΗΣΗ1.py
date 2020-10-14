a=list(10,10);
sum=0;
sum2=0;
sum3=0;
olsum=0;
for i in range(9):
 for j in range(9):
  if list (i,j)=="S":
   list.insert(i,j,"S")
  if list(i,j)=="0":
   continue
   list.insert(i,j,"O")
 else:
   continue
   print("DWSE TIMI S OR O")
   break
for i in range(9):
 for j in range(9):
  if j!=8 and j!=9 and list(i,j)=="S" and list(i,j)!=list(i,j+1)and list(i,j)==list(i,j+2):

   sum==sum+1
   for j in range(9):
    for i in range(9):
     if i!=8 and i!=9 and list(i,j)==S and list(i,j)!=list(i+1,j) and list(i,j)==list(i+2,j):
      sum2=sum2+1
for i in range(9):
 for j in range(9):
  if i!=8 and i!=9 and j!=8 and j!=9 and list(i,j)==S and list(i,j)!=list(i+1,j+1) and list(i,j)==list(i+2,j+2):
   sum3=sum3+1
olsum=sum+sum2+sum3
print(olsum)


          
            

