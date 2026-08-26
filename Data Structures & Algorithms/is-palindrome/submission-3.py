class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [ch.lower() for ch in s if ch.isalnum()]
        return all(l == r for l, r in zip(filtered[:(len(filtered) + 1) // 2], reversed(filtered)))