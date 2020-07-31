#!/usr/bin/env python3
# Jordan huang<good5dog5@gmail.com>

import os
import sys
import subprocess

class ListNode:
    def __init__(self, val = 0, next=None): 
        self.val = val
        self.next = next

def print_list(head):
    while(head):
        print(head.val, '->', end='')
        head = head.next
    print("null")

def swap_node(head):
    if head is None:
        return head

    dummy = ListNode(-1)
    dummy.next = head

    pre = dummy
    cur = dummy.next
    nex = None
    nnx = None


    if cur:
        nex = cur.next
    if nex:
        nnx = nex.next

    while(nex):

        pre.next = nex
        nex.next = cur
        cur.next = nnx

        pre = cur
        cur = nnx
        nex = None
        nnx = None
        if(cur):
            nex = cur.next
        if(nex):
            nnx = nex.next
    return dummy.next

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

a = swap_node(n1)
print_list(a)
