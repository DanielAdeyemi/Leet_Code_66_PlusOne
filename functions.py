class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join(str(digit) for digit in digits)
        num = str(int(num) + 1)
        num = [int(nu) for nu in num]
        return num
