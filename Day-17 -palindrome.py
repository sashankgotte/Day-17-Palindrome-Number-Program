
# Day 17: Palindrome Number Checker

n = int(input("Enter number: "))

if str(n) == str(n)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
