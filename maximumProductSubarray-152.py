# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 15:02:22 2021

@author: gauri
"""


#Maximum Product Subarray
nums = [2,3,-2,4]
nums = [-2,0,-1]
nums = [-3,-1,-1]
nums = [0,2]
nums = [-2,3,-4]
nums = [7,-2,-4]
nums = [3,-1,4]
nums = [-4,-3,-2]
if len(nums) == 0:
    print("empty array")
cur_max = cur_min = max_prod = nums[0]
for n in nums[1:]:
    print(n)
    temp = cur_max
    cur_max = max(cur_max * n, cur_min * n, n)
    print(cur_max)
    cur_min = min(cur_min * n, temp * n, n)
    print(cur_min)
    max_prod = max(max_prod, cur_max)
print(max_prod)
    
    