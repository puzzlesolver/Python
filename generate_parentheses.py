class Solution:
    def anagramMappings(self, A, B):
        D = {x: i for i, x in enumarate(B)}
        return [D[x] for x in A]