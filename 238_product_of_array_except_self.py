# -*- coding: utf-8 -*-
"""238_Product_of_Array_Except_Self.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gd_RXF1gscwan8MPcbm6X2YNJZ1zxK77

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product=[1]*n
        right_product=[1]*n
        result=[1]*n
        for i in range(1,n):
            left_product[i] = left_product[i-1]*nums[i-1]

        for i in range(n-2, -1, -1):
            right_product[i] = right_product[i+1]*nums[i+1]

        for i in range(n):
            result[i]= (left_product[i]*right_product[i])
        return (result)
result