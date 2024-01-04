class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hash_map = dict()
        ans = 0
        for n in nums:
            hash_map[n] = hash_map.get(n, 0) + 1
        for val in hash_map.values():
            if val == 1:
                return -1
            ans += ceil(val / 3)
        return ans
