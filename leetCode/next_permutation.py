#!/usr/bin/env python3
# Jordan huang<good5dog5@gmail.com>

import os
import sys
import unittest

# https://www.bookstack.cn/read/algorithm-exercise-tw/exhaustive_search-next_permutation.md
# ex :
# 6 5 4 8 7 5 1
# 首先肯定从后面开始看，1和5调换了没有用。
#
# 7、5和1调换了也没有效果，因此而发现了8、7、5、1是递减的。
#
# 如果想要找到下一个排列，找到递增的位置是关键。
#
# 因为在这里才可以使其增长得更大。
#
# 于是找到了4，显而易见4过了是5而不是8或者7更不是1。
#
# 因此就需要找出比4大但在这些大数里面最小的值，并将其两者调换。
#
# 那么整个排列就成了：6 5 5 8 7 4 1
#
# 然而最后一步将后面的8 7 4 1做一个递增。

# ----
# 1. 從後往前尋找索引滿足 a[k] < a[k + 1], 如果此條件不滿足，則說明已遍歷到最後一個。
# 2. 從後往前遍歷，找到第一個比a[k]大的數a[l], 即a[k] < a[l].
# 3. 交換a[k]與a[l].
# 4. 反轉k + 1 ~ n之間的元素。


def get_next_permutation(nums):
    if (len(nums) <= 1):
        return nums
    #1. From the back, find first i such that nums[i] > nums[i+1]
    reverse_idx = get_reverse_idx(nums)

    print(reverse_idx)

    if reverse_idx == len(nums) -1:
        return nums[::-1]

    last = nums[-1]
    
    for i in range(reverse_idx, len(nums)-1, 1):
        nums[i+1] = nums[i]
    nums[reverse_idx] = last

    return nums
        
def get_reverse_idx(nums):

    for i in range(len(nums)-1, 0, -1):
        if nums[i-1] < nums[i]:
            return i
    return 0

    #2. reverse from nums[i] ~ nums[-1]


next_perm = get_next_permutation([6,5,4,8,7,5,1])
print(next_perm)
