# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 19:41:56 2021

@author: gauri
"""


#Find Minimum in Rotated Sorted Array
nums = [3,4,5,1,2]
#nums = [4,5,6,7,0,1,2]
#nums = [11,13,15,17]
#nums.sort()
#print(nums[0])

left = 0
right = len(nums) - 1
while left < right:
    mid = left + (right - left) //2
    if nums[mid] > nums[right]:
        left = mid+1
    elif nums[mid] < nums[right]: 
        right = mid
    else:
        print(nums[right])
print(nums[left])