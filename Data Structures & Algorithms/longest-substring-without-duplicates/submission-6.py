class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0

        l, r  = 0, 0

        while l <= r < len(s):
            ch = s[r]
            if ch not in seen:
                r += 1
                seen.add(ch)
                max_len = max(max_len, r - l)
                continue

            while ch in seen:
                seen.remove(s[l])
                l += 1

        max_len = max(max_len, len(seen))
        return max_len
        