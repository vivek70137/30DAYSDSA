s = 'fEbiuewkjerk'

for i in range(len(s) - 1):
    if s[i].islower() and s[i+1].isupper():
        print(s)
        break  # Exit the loop after printing the string once if the condition is met
