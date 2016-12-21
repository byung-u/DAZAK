"""
Time: O(n)
Space: O(1)
[3] Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters

* Medium (23.23%)
* Total Submissions: 840173
* Total Accepted:    195379

Given a string,
find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""
# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-substring-without-repeating-characters.py


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest, start = 0, 0
        visited = [False for _ in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]:
                while char != s[start]:
                    # print('\t', char, s[start])
                    visited[ord(s[start])] = False
                    # print('\t', visited[ord(s[start])], s[start])
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True

            # print(longest, (i - start + 1), '____', i, '-', start, '+1')
            longest = max(longest, i - start + 1)
        return longest


if __name__ == '__main__':
    input_str = 'abcabcbb'
    print(Solution().lengthOfLongestSubstring(input_str))
