class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        b=[1]*len(a)
        for i in range(1,len(a)):
            b[i]=a[i-1]*b[i-1]
        
        tmp=1
        for i in range(len(a)-2,-1,-1):
            tmp*=a[i+1]
            b[i]*=tmp
        
        return b