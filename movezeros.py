def move_zeros(nums):
    s = []
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[s] = nums[i]
            s += 1
    while s < len(nums):
        nums[s] = 0
        s += 1
    return s

# Example usage:
##nums = [0, 1, 0, 3, 12]
##new_length = move_zeros(nums)
##print(nums)  # Output: [1, 3, 12, 0, 0]
##print(new_length)  # Output: 3
##def move_zeros(nums):
##    # Create a new list to store non-zero elements
##    non_zero_elements = [num for num in nums if num != 0]
##    
##    # Count the number of zeros
##    zero_count = len(nums) - len(non_zero_elements)
##    
##    # Extend the non-zero list with zeros
##    nums[:] = non_zero_elements + [0] * zero_count
##    
##    return len(non_zero_elements)
##
### Example usage:
##nums = [0, 1, 0, 3, 12]
##new_length = move_zeros(nums)
##print(nums)  # Output: [1, 3, 12, 0, 0]
##print(new_length)  # Output: 3
