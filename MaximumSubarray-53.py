# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 12:35:08 2021

@author: gauri
"""


#maximumSubArray
#nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
nums = [1]
nums = [-2,1]
nums = [-2,-1]

max_sum = nums[0]
cur_sum = 0
for n in nums:
    if cur_sum < 0:
        cur_sum = 0
    cur_sum = cur_sum + n
    max_sum = max(max_sum, cur_sum)
print(max_sum)