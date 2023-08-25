# -*- coding: utf-8 -*-
"""11. Container_With_Most_Water.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-Gx6KsYyZbO7-F7kNlUaZRN9cP-gK3OU

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j =len(height)-1
        max_area = 0
        while i<j:
            area = min(height[i], height[j])*(j-i)
            max_area= max(area, max_area)
            if height[i]>height[j]:
                j -= 1
            else:
                i +=1
        return(max_area)