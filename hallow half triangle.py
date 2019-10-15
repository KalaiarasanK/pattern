num = int(input())
for i in range(1,num+1):
    for j in range(i,num+1):
        if(i==1 or j==i or j==num):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()        
    
    
    
    #output
    
   5
   
* * * * * 
*     * 
*   * 
* * 
* 


num = int(input())
for i in range(1,num+1):
    for j in range(1,i+1):
        if(j==1 or j==i or i==num):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()        
    
    
    
    
    #output
    
    
* 
* * 
*   * 
*     * 
* * * * * 
