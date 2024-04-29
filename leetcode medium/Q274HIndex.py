class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        max_index = len(citations)
        for i in citations:
            if i<max_index:
                max_index-=1
        return max_index