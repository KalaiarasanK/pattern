#right triangle

num = int(input())
for i in range(1,num+1):
	for j in range(1,num+1):
		if(j <= num-i):
			print(" ",end=" ")
		else:
			print("*",end=" ")
	print()		
  
  
  output
  
  6
  
          * 
        * * 
      * * * 
    * * * * 
  * * * * * 
* * * * * * 
