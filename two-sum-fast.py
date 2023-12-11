from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      values_dict = { value: index for index,value in enumerate(nums)}
      for i in range(len(nums)):
          complement = target - nums[i]
          if complement in values_dict and i != values_dict[complement]:
              return [i, values_dict[complement]]


s = Solution()
s.twoSum([2,7,11,15],9)
