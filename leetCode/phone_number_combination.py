#!/usr/bin/env python3
# Jordan huang<good5dog5@gmail.com>

import os
import sys
import subprocess

mapping = {
    '0' : '',
    '1' : '',
    '2' : 'abc',
    '3' : 'def',
    '4' : 'ghi',
    '5' : 'jkl',
    '6' : 'mno',
    '7' : 'pqrs',
    '8' : 'tuv',
    '9' : 'wxyz'
}

def genCombination(digits, level, combination, result): 
    if (level == len(digits)):
        result.append(combination)
        return result

    option_char = mapping[digits[level]]
    print(option_char, combination, result)
    for i,c in enumerate(option_char):
        genCombination(digits, level+1, combination+c, result)


result = []
genCombination('23', 0, '', result)
print(result)
# print(genCombination('23', 0, '', result))
