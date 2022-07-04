#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums, target):
        print(f'nums are {nums}')
        print(f'target is {target}')
        for ind,num in enumerate(nums):
            for ind2,num2 in enumerate(nums):
                if ind == ind2:
                    continue
                if num + num2 == target:
                    return [ind,ind2]