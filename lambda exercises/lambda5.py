def fibo_seq(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibo_seq(n-1) + fibo_seq(n-2)) 
       
 
nth = int(input("Till which term "))  

if nth <= 0:  
   print("enter positive integers only")  
else:  
   print("sequence")  
   for i in range(nth):  
       print(fibo_seq(i)) 

