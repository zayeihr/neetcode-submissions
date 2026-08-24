class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        zero_count = nums.count(0)
        total_product = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                total_product = total_product * nums[i]

        for i in range(len(nums)):
            if zero_count == 0:
                output.append(total_product // nums[i])
            elif zero_count == 1:
                if nums[i] == 0:
                    output.append(total_product)
                else:
                    output.append(0)
            else:
                output.append(0)

        return output