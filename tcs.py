# a=[7,4,8,2,9]
# c=1
# m=a[0]
# for i in range(len(a)):
#     if a[i]>m:
#         c+=1
# print(c)        



from collections import Counter

def find_odd_balloon(balloons):
    # Count the frequency of each balloon color
    counter = Counter(balloons)
    
    # Check for any odd occurrences
    for balloon in balloons:
        if counter[balloon] % 2 != 0:
            return balloon
        else:
           return "All are even"

# Example usage
n = 7
balloons = ['r', 'g', 'b', 'b', 'g', 'y', 'y']
result = find_odd_balloon(balloons)
print(result)
