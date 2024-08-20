a = [1, 2, 1, 3, 4, 5]
b = [1, 2, 3, 4]
s = {}

# Count the occurrences of elements in `a`
for i in range(len(a)):
    if a[i] in s:
        s[a[i]] += 1
    else:
        s[a[i]] = 1

# Decrease the count for elements in `b`
for i in range(len(b)):
    if b[i] in s:
        s[b[i]] -= 1

# Collect and print the missing values
missing_values = [key for key in s if s[key] > 0]
print("Missing values:", missing_values)
