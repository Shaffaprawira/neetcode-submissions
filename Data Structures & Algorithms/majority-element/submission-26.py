class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # counter = 0
        nums_set = {}
        # for k,v in enumerate(nums):

        for n in nums:
            if n not in nums_set:
                nums_set[n] = 1
            else:
                nums_set[n] += 1

        max_count = max(n[1] for n in nums_set.items())
        
        for i in nums_set.items():
            if i[1] == max_count:
                return i[0]
        
        # return nums_set.values()


        # for n in nums_set.items():
            # print(n[1])
            # print(n.keys())
            # print(n.values())

        # print(nums_set.keys())
        # print(nums_set.values())
        # print(nums_set.items())
        # print(max(nums_set.keys()))
        # print(max(nums_set.values()))
        # print(max(nums_set.items()))
        # return max(nums_set.values())

