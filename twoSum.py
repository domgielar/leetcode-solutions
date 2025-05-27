class Solution(object):
    def twoSum(self, nums, target):
        numlen = len(nums)
        for i in range(0,numlen-1):
            if nums[i] + nums[i+1] == target:
                arr = []
                arr.append(i)
                arr.append(i+1)
                return arr
        print("There are no two elemnts consecutively that add up to the target.")
                
                
nums = [2, 3, 4, 6, 1, 7, 2]
target = 9

sol = Solution()
result = sol.twoSum(nums, target)
print(result)