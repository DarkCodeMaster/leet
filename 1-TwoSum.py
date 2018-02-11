class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return False
        temp = {}
        for i in range(len(nums)):
                #temp[i] = target-nums[i]
                temp[(target-nums[i])] = i
        print(temp)
        for i in range(len(nums)):
            if nums[i] in temp:
                if i != temp[nums[i]]:
                    return[i, temp[nums[i]]]
