class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s=set(nums)
        s=sorted(s)
        print(s)
        mc=1
        c=1
        l=0
        r=1
        if not  s : return 0
        while r<=len(s)-1:
            if s[r]-s[l]==1:
                c+=1
            else:
                c=1
            mc=max(c,mc)
            
            l+=1
            r+=1
        
        return mc


                
                