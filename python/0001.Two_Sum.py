# -*- coding: utf-8 -*-
"""
Created on Jan 5 2021

@author: zqq

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出 "和 "为目标值的那两个整数，
并返回他们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
例如：
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""

# # 方法1：暴力求解
# class Solution(object):
#     def twoSum(self,nums,target):
#         """
#         :param nums: List[int]
#         :param target: int
#         :return: List[int]
#         时间复杂度: O(n^2)
#         空间复杂度：O(1)
#         """
#         ns = len(nums)
#         for i in range(0,ns):
#             for j in range(i+1,ns):
#                 if nums[i]+nums[j]==target:
#                     return [i,j]


# 方法2：引入map
class Solution(object):
    def twoSum(self,nums,target):
        """
        时间复杂度：O(n)
        :param nums:
        :param target:
        :return:
        """
        Dict = {} # 定义一个空字典，用于存放key-value
        for i in range(0,len(nums)): # 注：可以用 for index，value in enumerate(nums)
            # print(i)
            value = target - nums[i]
            # print("value: ",value)
            if value in Dict:
                # print([Dict[value],i])
                return [Dict[value],i]
            else:
                Dict[nums[i]]=i
            # print(Dict)
        


# if __name__ == "__main__":
#     s = Solution()
#     res = s.twoSum([2,4,7,3,5],10)
#     print(res)
