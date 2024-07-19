def getMaxValue(arr):
    # Step 1: Sort the array
    arr.sort()  # Sorting the array to easily manage the constraints
    
    # Step 2: Ensure the first element is 1
    arr[0] = 1  # Setting the first element to 1 as required
    
    # Step 3: Adjust each subsequent element
    for i in range(1, len(arr)):  # Iterate over the array starting from the second element
        if arr[i] > arr[i-1] + 1:  # If the current element is more than 1 greater than the previous element
            arr[i] = arr[i-1] + 1  # Set the current element to be 1 greater than the previous element
    
    # The maximum value of the final element is the answer
    return arr  # Return the last element of the adjusted array

# Example usage
arr = [9,3 ,5,34]
print(getMaxValue(arr))  # Expected Output: 4
