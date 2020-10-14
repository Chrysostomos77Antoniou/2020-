a=list(range(10,10));
sum=0;
sum2=0;
sum3=0;
olsum=0;
athroisma=0;
if athroisma==0:
 for i in range(9):
  for j in range(9):
   while a[i,j] is None:
    if j%2==1:
     continue
     a.insert[i,j,1]
    elif j%2==0:
     continue
     a.insert[i,j,0]
 for i in range(9):
  for j in range(9):
   if a[i,j]==1 or a[i,j]==0:
    continue
    if j!=7 and j!=8 and a[i,j]==a[i,j+1] and a[i,j]==a[i,j+2] and a[i,j]==a[i,j+3]:
      continue
      sum=sum+1
 for j in range(9):
  for i in range(9):
   if a[i,j]==1 or a[i,j]==0:
    continue
    if i!=7 and i!=8 and i!=9 and a[i,j]==1 or a[i,j]==0:
     continue
     sum2=sum2+1
 for i in range in (9):
  for j in range(9):
   while a[i,j]==1 or a[i,j]==0:
    if i!=7 and i!=8 and i!=9 and j!=7 and j!=8 and j!=9: 
     continue
     if a[i,j]==S and a[i,j]!=a[i+1,j+1] and a[i,j]==a[i+2,j+2]:
      sum3=sum3+1
      olsum=sum+sum2+sum3;
      break
if olsum==0:
    del a
    athroisma=athroisma+1
    print("ΔΩΣΕ ΝΕΑ ΣΤΟΙΧΕΙΑ ΓΙΑ ΠΙΝΑΚΑ")
else:
    print
print(olsum)
