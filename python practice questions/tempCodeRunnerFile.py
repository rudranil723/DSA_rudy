n=int(input("Enter the number of strings: ")) 
d={} 
print("Input strings") 
for i in range(1,n+1,1): 
 s=input() 
 d[s]=len(s) 
print("\nDictionary:", d)