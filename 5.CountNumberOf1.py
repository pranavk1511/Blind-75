class Solution:
    def hammingWeight(self, n: int) -> int:
        n=str(bin(n)) #Convert  to Binary to String 
        count=0
        for i in range(len(n)): 
            if n[i] == '1':  #Check for each occurence of 1 and increment the       counter 
                count=count+1
        # print(count)   
        
        
        return count 