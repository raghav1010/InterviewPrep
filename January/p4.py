#1009. Complement of Base 10 Integer
class Solution:
    def bitwiseComplement(self, N):
        return (1 << N.bit_length()) - 1 - N if N else 1