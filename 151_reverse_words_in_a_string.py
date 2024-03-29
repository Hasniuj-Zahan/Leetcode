# -*- coding: utf-8 -*-
"""151_Reverse_Words_in_a_String.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P4m8vzysbaC2TcHxDw42M1OIqCKQtylX

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        result = ''
        x = s.split()
        for i in range(len(x)):
            if i ==len(x) or i== 0:
                result = x[i] + result
            else:
                result = x[i] + ' ' + result
        return result