data = input().split(", ")
nums = [int(nums) for nums in data]
result = [index for index in range(len(nums)) if nums[index] % 2 == 0]
print(result)
