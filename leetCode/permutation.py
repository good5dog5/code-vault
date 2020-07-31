#!/usr/bin/env python3
# Jordan huang<good5dog5@gmail.com>

import os
import sys
import subprocess

# Input: [1,1,2]
# Output:
#     [
#       [1,1,2],
#       [1,2,1],
#       [2,1,1]
#     ]


def rotate(input, level, is_visited, combination, result):
    if (level == len(is_visited)):
        result.append(combination[:])
        return result

    for i,c in enumerate(input):
        if not is_visited[i]:
            is_visited[i] = True
            combination.append(input[i])
            rotate(input, level+1, is_visited, combination, result)
            is_visited[i] = False
            combination.pop()

result = []
combination =[] 

input = [1,2,3]
rotate(input, 0, [False] * len(input), combination, result)
print(result)


