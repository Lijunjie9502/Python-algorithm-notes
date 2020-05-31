class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return False

        for num in nums:
            if num < 0 or num > len(nums) - 1:
                return Flase

        start, end = 1, len(nums) - 1
        while start <= end:
            middle = (start + end) >> 1
            counts = self.countRange(nums, start, middle)
            if start == end:
                if counts > 1:
                    return start
                else:
                    break
            
            if counts > middle - start + 1:
                end = middle
            else:
                start = middle + 1
        return False
                
    @staticmethod
    def countRange(nums, start, end):
        """
        统计　nums 中在　[start, end] 区间内的元素数目
        """
        sums = 0
        for num in nums:
            if start <= num <= end:
                sums += 1
        return sums