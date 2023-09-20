assert longest_substring_with_k_distinct_characters('abaccc', 3) == 'ccc'
  assert longest_substring_with_k_distinct_characters('aabcbcbb', 2) == 'bcb'


def longest_substring_with_k_distinct_characters(string, k):
 Both the string and k will be passed in by the test. 
 Your function should return the longest substring of the string with k distinct characters. 
 If there are multiple longest substrings, return one of them. 
 If there is no substring with k distinct characters, return an empty string.