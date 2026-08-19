class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_set = {}

        for n in nums:
            if n not in nums_set:
                nums_set[n] = 1
            else:
                nums_set[n] += 1

        max_count = max(n[1] for n in nums_set.items())
        
        for i in nums_set.items():
            if i[1] == max_count:
                return i[0]