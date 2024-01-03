class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = 0
        device_count = 0
        for row in bank:
            device_count = row.count("1")
            if device_count:
                ans = ans + prev*device_count
                prev = device_count
        return ans
