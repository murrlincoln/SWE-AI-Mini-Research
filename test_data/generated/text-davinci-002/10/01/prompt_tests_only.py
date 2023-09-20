- Input: 0
  Expected Output: 1
- Input: -5
  Expected Output: ValueError

def factorial(n):
    if n < 0: 
        raise ValueError("Input must be a non-negative integer")
    elif n == 0: 
        return 1
    else: 
        return n * factorial(n - 1)