# Set the counters to 0
even = 0
odd = 0
# Ask the user to enter three whole numbers
first = int(input("Please enter the first whole number.\n"))
second = int(input("Please enter the second whole number.\n"))
third = int(input("Please enter the third whole number.\n"))
# Check the first number
if first % 2 == 0:
   even = even + 1
else:
   odd = odd + 1
# Check the second number
if second % 2 == 0:
    even = even + 1
else:
    odd = odd + 1
# Check the third number
if third % 2 == 0:
   even = even + 1
else:
   odd = odd + 1
# Display the results
print("There were", even, "even and", odd, "odd numbers.")