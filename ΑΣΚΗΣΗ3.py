import random
print("ΑΣ ΠΑΙΞΟΥΜΕ ΕΝΑ ΠΑΙΧΝΙΔΙ")
word=(input("ΔΩΣΕ ΛΕΞΗ: "))
a=list(word);
b=[];
sum3=0;
#ΔΕΝ ΥΠΑΡΧΕΙ ΛΕΞΗ ΠΟΥ ΕΧΕΙ ΠΑΝΩ ΑΠΟ 10000 ΑΝΑΓΡΑΜΜΑΤΙΣΜΟΥΣ#
for j in range(10000):
    random.shuffle(a)
    result=''.join(a)
    if b.count(result)==0:
     continue
    sum3=sum3+1
    b.insert(sum3,result)
print(b)

      

   

  


    
    
