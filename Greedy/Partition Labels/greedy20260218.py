class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_appearance = {}
        for i, alphabet in enumerate(s):
            last_appearance[alphabet] = i
        start = 0
        current_maximal_last_appearance = 0
        res = []
        for end in range(len(s)):
            current_maximal_last_appearance = max(current_maximal_last_appearance, last_appearance[s[end]])
            if end==current_maximal_last_appearance:
                res.append(end-start+1)
                start = end+1
        return res