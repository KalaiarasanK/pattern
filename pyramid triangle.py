#pyramid


num = int(input())
for i in range(num):
	for j in range(num-i):
		print("",end=" ")
	for j in range((2*i)+1):
		print("*",end="")
	print(end="\n")		
  
  
  
  #output
  
  5
  
     *
    ***
   *****
  *******
 *********
