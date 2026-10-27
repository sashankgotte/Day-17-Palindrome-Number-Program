# Day 17: Palindrome Number Checker 🐍

## 📌 Description
This Python program checks whether a given number is a palindrome. A palindrome number remains the same when its digits are reversed.

## 💻 Python Code
```python
n = int(input("Enter number: "))

if str(n) == str(n)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

## ▶️ Example Output

**Example 1:**
```text
Enter number: 121
Palindrome
```

**Example 2:**
```text
Enter number: 123
Not Palindrome
```

## 🧠 Concepts Learned
- User input using `input()`
- Type conversion using `str()`
- String slicing using `[::-1]`
- Conditional statements (`if-else`)
- Palindrome number logic

## 🎯 Learning Outcome
Learned how to reverse a number's string representation and check whether it matches the original number.

## 📅 Challenge Progress
**100 Days of Python Programming — Day 17/100**

---
⭐ Practicing Python every day to improve my programming and problem-solving skills.