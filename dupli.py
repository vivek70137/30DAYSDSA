# Function to print unique elements in the same order as they appear in the input
def print_unique_elements(arr):
    # Create an empty set to store unique elements
    unique_set = set()
    # Create a set to store repeated elements
    repeated_set = set()
    
    # Iterate through the array
    for num in arr:
        # If the element is in the unique set, it's a repeated number
        if num in unique_set:
            repeated_set.add(num)
        else:
            # Add the element to the unique set
            unique_set.add(num)
    
    # Print the unique elements that are not repeated
    for num in arr:
        if num not in repeated_set:
            print(num, end=" ")

# Main function
if __name__ == "__main__":
    # Input the size of the array
    N = int(input())
    
    # Input the array elements
    arr = list(map(int, input().split()))
    
    # Call the function to print unique elements
    print_unique_elements(arr)

