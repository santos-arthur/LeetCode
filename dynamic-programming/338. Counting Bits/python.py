class Solution:
    def countBits(self, n: int) -> List[int]:
        return[ list((bin(n)[2:])).count('1') for n in range(n+1)]
