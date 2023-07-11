class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         longest_len = -1
         left = 0
         right = 0
         res = 0
         visited = []
         if s == "":
             return 0
         while right < len(s):
             current = s[right]            
             if current not in set(s[left:right]): # this can replaces with set
                 right += 1
                 longest_len = max(longest_len, right - left)
             else: # encountered duplicate
                 while s[left] != current:
                     left += 1
                 right += 1 # increment it once remove duplicate 
                 left += 1 # to remove duplicate

         return longest_len
        