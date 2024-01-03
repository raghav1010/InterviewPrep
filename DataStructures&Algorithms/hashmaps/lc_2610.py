class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hash_map = dict()
        max_freq = 0
        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1
            max_freq = max(max_freq, hash_map[i])

        matrix = [[] for i in range(max_freq)]
        for i in nums:
            while hash_map[i] > 0:
                matrix[hash_map[i] - 1].append(i)
                hash_map[i] -= 1
        return matrix
