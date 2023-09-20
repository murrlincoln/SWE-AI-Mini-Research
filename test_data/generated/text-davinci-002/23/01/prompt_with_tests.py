- Input: 'abaccc', k = 3
  Expected Output: 'ccc'

def longestSubstring(s, k) -> str:
        left = 0
        hash_map = {}
        max_length = 0
        start = 0
        result = ''
        
        for right in range(len(s)):
            hash_map[s[right]] = right
            
            if len(hash_map) == k + 1:
                delete_index = min(hash_map.values())
                del hash_map[s[delete_index]]
                left = delete_index + 1
                
            if max_length < right - left:
                max_length = right - left
                start = left
        
        return s[start : start + max_length]