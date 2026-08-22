class Solution:
    def encode(self, strs: List[str]) -> str:
        return ';;'.join(
            '"' + s.replace(';', r'\;') + '"' for s in strs
        )

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        return [
            ss.replace(r'\;', ';')[1:-1]
            for ss in s.split(';;')
        ]