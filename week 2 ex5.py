first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

#The program should then decide which of the two numbers is the smallest and display the message
# "The first number is the smallest!" if the first number is smaller,
# "The second number is the smallest!" if the second number is smaller or
# "Both are equal!" if both numbers are equal in value.
if first_num < second_num:
    print(f"The first number is the smallest!")
elif second_num < first_num:
    print(f"The second number is the largest!")
else:
    print(f"Both are equal!")
