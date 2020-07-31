#!/usr/bin/env python3
# Jordan huang<good5dog5@gmail.com>

import os
import sys
import subprocess

def twoSum(nums, target):
    pair = {} 
    for i,n in enumerate(nums):
        if (n) in pair.keys():
            return [pair[n], i]
        else:
            pair[target-n] = i
        

print(twoSum([2, 7, 11, 15], 9))
