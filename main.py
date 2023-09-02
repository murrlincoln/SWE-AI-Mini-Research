from typing import List, Dict
import re

def sort_even_numbers(arr: List[int]) -> List[int]:
    """
    Sorts the even numbers in the given list in ascending order,
    while leaving the odd numbers in their original positions.

    Parameters:
    - arr: List[int] - The input list of integers.

    Returns:
    - List[int] - The modified list with sorted even numbers.
    """
    pass  # Your implementation here

# Test functions
def test_sort_even_numbers():
    assert sort_even_numbers([5, 3, 2, 8, 1, 4]) == [5, 3, 2, 8, 1, 4]
    assert sort_even_numbers([0, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_even_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9, 0, 7, 2, 5, 4, 3, 6, 1, 8]
    assert sort_even_numbers([1, 3, 5, 7]) == [1, 3, 5, 7]
    assert sort_even_numbers([]) == []



def reverse_vowels(s: str) -> str:
    """
    Reverses the vowels in a given string.

    Parameters:
    - s: str - The input string.

    Returns:
    - str - The modified string with reversed vowels.
    """
    pass  # Your implementation here

# Test functions
def test_reverse_vowels():
    assert reverse_vowels("hello") == "holle"
    assert reverse_vowels("world") == "world"
    assert reverse_vowels("leetcode") == "leotcede"
    assert reverse_vowels("aeiou") == "uoiea"
    assert reverse_vowels("") == ""



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    """
    Reverses a singly linked list.

    Parameters:
    - head: ListNode - The head node of the linked list.

    Returns:
    - ListNode - The head node of the reversed linked list.
    """
    pass  # Your implementation here

# Helper function to convert linked list to list
def linked_list_to_list(head: ListNode) -> list:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

# Test functions
def test_reverse_linked_list():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_list(reversed_head) == [4, 3, 2, 1]

    head = ListNode(1)
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_list(reversed_head) == [1]

    head = None
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_list(reversed_head) == []


def fibonacci_recursive(n: int) -> int:
    """
    Calculates the nth Fibonacci number using recursion.

    Parameters:
    - n: int - The position of the Fibonacci number to find (0-indexed).

    Returns:
    - int - The nth Fibonacci number.
    """
    pass  # Your implementation here

# Test functions
def test_fibonacci_recursive():
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(2) == 1
    assert fibonacci_recursive(3) == 2
    assert fibonacci_recursive(4) == 3
    assert fibonacci_recursive(5) == 5




def max_product_of_two(nums: List[int]) -> int:
    """
    Finds the maximum product of any two integers in a given list.

    Parameters:
    - nums: List[int] - The list of integers.

    Returns:
    - int - The maximum product of any two integers in the list.
    """
    pass  # Your implementation here

# Test functions
def test_max_product_of_two():
    assert max_product_of_two([1, 2, 3, 4]) == 12
    assert max_product_of_two([-1, -2, -3, -4]) == 12
    assert max_product_of_two([0, 0, 0, 0]) == 0
    assert max_product_of_two([1]) == None
    assert max_product_of_two([]) == None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root: TreeNode) -> bool:
    """
    Checks if a binary tree is balanced.

    Parameters:
    - root: TreeNode - The root node of the binary tree.

    Returns:
    - bool - True if the tree is balanced, False otherwise.
    """
    pass  # Your implementation here

# Test functions
def test_is_balanced():
    root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert is_balanced(root1) == True
    
    root2 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6)), TreeNode(5)), TreeNode(3))
    assert is_balanced(root2) == False

    assert is_balanced(None) == True



def validate_email(email: str) -> bool:
    """
    Validates an email address according to the following rules:
    - It should have the '@' symbol.
    - It should have a domain name after the '@' symbol.
    - The domain name should end with '.com'.

    Parameters:
    - email: str - The email address to validate.

    Returns:
    - bool - True if the email is valid, False otherwise.
    """
    pass  # Your implementation here

# Test functions
def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("test.example.com") == False
    assert validate_email("test@") == False
    assert validate_email("@example.com") == False
    assert validate_email("") == False


def range_bitwise_and(m: int, n: int) -> int:
    """
    Calculates the bitwise AND of all numbers from m to n, both inclusive.

    Parameters:
    - m: int - Start of the range.
    - n: int - End of the range.

    Returns:
    - int - Bitwise AND of all numbers in the range [m, n].
    """
    pass  # Your implementation here

# Test functions
def test_range_bitwise_and():
    assert range_bitwise_and(5, 7) == 4
    assert range_bitwise_and(0, 1) == 0
    assert range_bitwise_and(1, 1) == 1
    assert range_bitwise_and(0, 0) == 0



def bubble_sort(arr: List[int]) -> List[int]:
    """
    Sorts an array using the bubble sort algorithm.

    Parameters:
    - arr: List[int] - The array to be sorted.

    Returns:
    - List[int] - The sorted array.
    """
    pass  # Your implementation here

# Test functions
def test_bubble_sort():
    assert bubble_sort([5, 3, 1, 4, 6]) == [1, 3, 4, 5, 6]
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubble_sort([]) == []



def depth_first_search(graph: Dict[int, List[int]], start: int) -> List[int]:
    """
    Performs a depth-first search on a graph represented as an adjacency list.

    Parameters:
    - graph: Dict[int, List[int]] - The adjacency list representing the graph.
    - start: int - The starting vertex.

    Returns:
    - List[int] - The vertices visited in DFS order.
    """
    pass  # Your implementation here

# Test functions
def test_depth_first_search():
    assert depth_first_search({1: [2, 3], 2: [4], 3: [], 4: []}, 1) == [1, 2, 4, 3]
    assert depth_first_search({1: [2, 3], 2: [1], 3: [1]}, 1) == [1, 2, 3]
    assert depth_first_search({}, 1) == []


def factorial_recursive(n: int) -> int:
    """
    Calculates the factorial of a given number using recursion.

    Parameters:
    - n: int - The number for which the factorial is to be calculated.

    Returns:
    - int - The factorial of the given number.
    """
    pass  # Your implementation here

# Test functions
def test_factorial_recursive():
    assert factorial_recursive(5) == 120
    assert factorial_recursive(1) == 1
    assert factorial_recursive(0) == 1
    assert factorial_recursive(6) == 720



# --- CLAUDE LIST --- #
# multiply_list
def multiply_list(nums):
  pass

def test_empty():
  nums = []
  assert multiply_list(nums) == 1

def test_single():
  nums = [2]
  assert multiply_list(nums) == 2
  
def test_multi():
  nums = [1, 2, 3]
  assert multiply_list(nums) == 6

# count_vowels  
def count_vowels(text):
  pass

def test_empty():
  text = ''
  assert count_vowels(text) == 0

def test_no_vowels():
  text = 'try'
  assert count_vowels(text) == 0

def test_multi():
  text = 'apple'
  assert count_vowels(text) == 2

# is_palindrome
def is_palindrome(text):
  pass

def test_empty():
  text = ''
  assert is_palindrome(text) == True

def test_not_palindrome():
  text = 'hello'
  assert is_palindrome(text) == False

def test_palindrome():
  text = 'racecar'
  assert is_palindrome(text) == True
  
# longest_word  
def longest_word(sentence):
  pass

def test_empty():
  sentence = ''
  assert longest_word(sentence) == ''

def test_single():
  sentence = 'hi'
  assert longest_word(sentence) == 'hi'

def test_multi():
  sentence = 'hello there my friend'
  assert longest_word(sentence) == 'hello'
  
# capitalize
def capitalize(text):
  pass

def test_empty():
  text = ''
  assert capitalize(text) == ''

def test_single():
  text = 'hello'
  assert capitalize(text) == 'Hello'

def test_multi():
  text = 'hello world'
  assert capitalize(text) == 'Hello World'

# reverse_string
def reverse_string(text):
  pass

def test_empty():
  text = ''
  assert reverse_string(text) == ''

def test_single():
  text = 'a' 
  assert reverse_string(text) == 'a'

def test_multi():
  text = 'abc'
  assert reverse_string(text) == 'cba'

# count_digits
def count_digits(num):
  pass

def test_zero():
  num = 0
  assert count_digits(num) == 1
  
def test_single():
  num = 5
  assert count_digits(num) == 1

def test_multi():
  num = 348
  assert count_digits(num) == 3
  
# factorial 
def factorial(num):
  pass

def test_zero():
  num = 0
  assert factorial(num) == 1

def test_single():
  num = 1
  assert factorial(num) == 1

def test_multi():
  num = 5
  assert factorial(num) == 120
  
# fibonacci
def fibonacci(num):
  pass

def test_zero():
  num = 0
  assert fibonacci(num) == [0] 

def test_one():
  num = 1
  assert fibonacci(num) == [0, 1]
  
def test_multi():
  num = 6
  assert fibonacci(num) == [0, 1, 1, 2, 3, 5]
  
# fizzbuzz
def fizzbuzz(num):
  pass

def test_fizz():
  num = 3
  assert fizzbuzz(num) == 'Fizz'

def test_buzz():
  num = 5
  assert fizzbuzz(num) == 'Buzz'

def test_fizzbuzz():
  num = 15
  assert fizzbuzz(num) == 'FizzBuzz'

# --- BARD ---
def find_first_non_repeating_char(s: str) -> str:
    pass

def test_find_first_non_repeating_char():
    assert find_first_non_repeating_char('abca') == 'b'
    assert find_first_non_repeating_char('ccbaab') == 'b'
    assert find_first_non_repeating_char('aabbcc') == ''
    assert find_first_non_repeating_char('z') == 'z'

def find_longest_substring_without_repeating_characters(s: str) -> str:
    pass

def test_find_longest_substring_without_repeating_characters():
    assert find_longest_substring_without_repeating_characters('abcabcbb') == 'abc'
    assert find_longest_substring_without_repeating_characters('bbbbb') == 'b'
    assert find_longest_substring_without_repeating_characters('pwwkew') == 'wke'
    assert find_longest_substring_without_repeating_characters('') == ''

def longest_substring_with_k_distinct_characters(s: str, k: int) -> str:
    pass

def test_longest_substring_with_k_distinct_characters():
    assert longest_substring_with_k_distinct_characters('abcabcbb', 2) == 'abc'
    assert longest_substring_with_k_distinct_characters('bbbbb', 3) == ''
    assert longest_substring_with_k_distinct_characters('pwwkew', 3) == 'wke'
    assert longest_substring_with_k_distinct_characters('', 2) == ''

def longest_palindromic_substring(s: str) -> str:
    pass

def test_longest_palindromic_substring():
    assert longest_palindromic_substring('babad') == 'bab'
    assert longest_palindromic_substring('cbbd') == 'bb'
    assert longest_palindromic_substring('a') == 'a'
    assert longest_palindromic_substring('') == ''

def longest_common_substring(s1: str, s2: str) -> str:
    pass

def test_longest_common_substring():
    assert longest_common_substring('abcde', 'bcde') == 'bcde'
    assert longest_common_substring('abcdef', 'abef') == 'abe'
    assert longest_common_substring('abc', '') == ''
    assert longest_common_substring('', 'abc') == ''
