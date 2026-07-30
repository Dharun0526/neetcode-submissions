class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        b=[]
        for i in nums:
            if i in b:
                return True

            b.append(i)
        return False
           