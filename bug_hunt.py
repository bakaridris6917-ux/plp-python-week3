count = 1
total = 0

# BUG: The while line was missing a colon at the end, causing a syntax error. I added the colon.
# BUG: The condition count < 5 stopeed the loop before adding 5, so the program printed 10 instead of 15 with no error. I changed it to count <= 5 so 5 is included.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: total is an integer, and python cannot join a string and an integer with +, which caused a TypeError. I wrapped total in str() to convert it to text.
print("Sum of 1 to 5 is: " + str(total))
