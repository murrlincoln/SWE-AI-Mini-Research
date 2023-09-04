import unittest
import main

def linked_list_to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values

class TestCodingProblems(unittest.TestCase):

    def test_sort_even_numbers(self):
        self.assertEqual(main.sort_even_numbers([5, 3, 2, 8, 1, 4]), [5, 3, 2, 4, 1, 8])
        self.assertEqual(main.sort_even_numbers([0, 1, 2, 3, 4, 5]), [0, 1, 2, 3, 4, 5])
        self.assertEqual(main.sort_even_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), [9, 0, 7, 2, 5, 4, 3, 6, 1, 8])
        self.assertEqual(main.sort_even_numbers([1, 3, 5, 7]), [1, 3, 5, 7])
        self.assertEqual(main.sort_even_numbers([]), [])

    def test_reverse_vowels(self):
        self.assertEqual(main.reverse_vowels("hello"), "holle")
        self.assertEqual(main.reverse_vowels("world"), "world")
        self.assertEqual(main.reverse_vowels("leetcode"), "leotcede")
        self.assertEqual(main.reverse_vowels("aeiou"), "uoiea")
        self.assertEqual(main.reverse_vowels(""), "")

    def test_reverse_linked_list(self):
        # Create linked list 1 -> 2 -> 3 -> 4
        head = main.ListNode(1, main.ListNode(2, main.ListNode(3, main.ListNode(4))))
        reversed_head = main.reverse_linked_list(head)
        self.assertEqual(linked_list_to_list(reversed_head), [4, 3, 2, 1])

        # Create linked list with one node: 1
        head = main.ListNode(1)
        reversed_head = main.reverse_linked_list(head)
        self.assertEqual(linked_list_to_list(reversed_head), [1])

        # Create empty linked list
        head = None
        reversed_head = main.reverse_linked_list(head)
        self.assertEqual(linked_list_to_list(reversed_head), [])

    def test_fibonacci_recursive(self):
        self.assertEqual(main.fibonacci_recursive(0), 0)
        self.assertEqual(main.fibonacci_recursive(1), 1)
        self.assertEqual(main.fibonacci_recursive(2), 1)
        self.assertEqual(main.fibonacci_recursive(3), 2)
        self.assertEqual(main.fibonacci_recursive(4), 3)
        self.assertEqual(main.fibonacci_recursive(5), 5)

    def test_max_product_of_two(self):
        self.assertEqual(main.max_product_of_two([1, 2, 3, 4]), 12)
        self.assertEqual(main.max_product_of_two([-1, -2, -3, -4]), 12)
        self.assertEqual(main.max_product_of_two([0, 0, 0, 0]), 0)
        self.assertEqual(main.max_product_of_two([1]), None)
        self.assertEqual(main.max_product_of_two([]), None)
        
    def test_is_balanced(self):
        # Create balanced tree
        root1 = main.TreeNode(1, main.TreeNode(2, main.TreeNode(4), main.TreeNode(5)), main.TreeNode(3))
        self.assertEqual(main.is_balanced(root1), True)

        # Create unbalanced tree
        root2 = main.TreeNode(1, main.TreeNode(2, main.TreeNode(4, main.TreeNode(6)), main.TreeNode(5)), main.TreeNode(3))
        self.assertEqual(main.is_balanced(root2), False)

        # Test empty tree
        self.assertEqual(main.is_balanced(None), True) 

    def test_validate_email(self):
        self.assertEqual(main.validate_email("test@example.com"), True)
        self.assertEqual(main.validate_email("test.example.com"), False)
        self.assertEqual(main.validate_email("test@"), False)
        self.assertEqual(main.validate_email("@example.com"), False)
        self.assertEqual(main.validate_email(""), False)

    def test_range_bitwise_and(self):
        self.assertEqual(main.range_bitwise_and(5, 7), 4)
        self.assertEqual(main.range_bitwise_and(0, 1), 0)
        self.assertEqual(main.range_bitwise_and(1, 1), 1)
        self.assertEqual(main.range_bitwise_and(0, 0), 0)

    def test_bubble_sort(self):
        self.assertEqual(main.bubble_sort([5, 3, 1, 4, 6]), [1, 3, 4, 5, 6])
        self.assertEqual(main.bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(main.bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(main.bubble_sort([]), [])

    def test_depth_first_search(self):
        self.assertEqual(main.depth_first_search({1: [2, 3], 2: [4], 3: [], 4: []}, 1), [1, 2, 4, 3])
        self.assertEqual(main.depth_first_search({1: [2, 3], 2: [1], 3: [1]}, 1), [1, 2, 3])
        self.assertEqual(main.depth_first_search({}, 1), [])

    def test_factorial_recursive(self):
        self.assertEqual(main.factorial_recursive(5), 120)
        self.assertEqual(main.factorial_recursive(1), 1)
        self.assertEqual(main.factorial_recursive(0), 1)
        self.assertEqual(main.factorial_recursive(6), 720)
        
    def test_empty():
        nums = []
        assert main.multiply_list(nums) == 1

    def test_single():
        nums = [2]
        assert main.multiply_list(nums) == 2
  
    def test_multi():
        nums = [1, 2, 3]
        assert main.multiply_list(nums) == 6

    def test_empty_count_vowels(self):
        text = ''
        self.assertEqual(main.count_vowels(text), 0)

    def test_no_vowels(self):
        text = 'try'
        self.assertEqual(main.count_vowels(text), 0)

    def test_multi_count_vowels(self):
        text = 'apple'
        self.assertEqual(main.count_vowels(text), 2)

    # For is_palindrome
    def test_empty_is_palindrome(self):
        text = ''
        self.assertEqual(main.is_palindrome(text), True)

    def test_not_palindrome(self):
        text = 'hello'
        self.assertEqual(main.is_palindrome(text), False)

    def test_palindrome(self):
        text = 'racecar'
        self.assertEqual(main.is_palindrome(text), True)

    # For longest_word
    def test_empty_longest_word(self):
        sentence = ''
        self.assertEqual(main.longest_word(sentence), '')

    def test_single_longest_word(self):
        sentence = 'hi'
        self.assertEqual(main.longest_word(sentence), 'hi')

    def test_multi_longest_word(self):
        sentence = 'hello there my friend'
        self.assertEqual(main.longest_word(sentence), 'hello')

    # For capitalize
    def test_empty_capitalize(self):
        text = ''
        self.assertEqual(main.capitalize(text), '')

    def test_single_capitalize(self):
        text = 'hello'
        self.assertEqual(main.capitalize(text), 'Hello')

    def test_multi_capitalize(self):
        text = 'hello world'
        self.assertEqual(main.capitalize(text), 'Hello World')

    # For reverse_string
    def test_empty_reverse_string(self):
        text = ''
        self.assertEqual(main.reverse_string(text), '')

    def test_single_reverse_string(self):
        text = 'a'
        self.assertEqual(main.reverse_string(text), 'a')

    def test_multi_reverse_string(self):
        text = 'abc'
        self.assertEqual(main.reverse_string(text), 'cba')

    # For count_digits
    def test_zero_count_digits(self):
        num = 0
        self.assertEqual(main.count_digits(num), 1)

    def test_single_count_digits(self):
        num = 5
        self.assertEqual(main.count_digits(num), 1)

    def test_multi_count_digits(self):
        num = 348
        self.assertEqual(main.count_digits(num), 3)

    # For factorial
    def test_zero_factorial(self):
        num = 0
        self.assertEqual(main.factorial(num), 1)

    def test_single_factorial(self):
        num = 1
        self.assertEqual(main.factorial(num), 1)

    def test_multi_factorial(self):
        num = 5
        self.assertEqual(main.factorial(num), 120)

    # For fibonacci
    def test_zero_fibonacci(self):
        num = 0
        self.assertEqual(main.fibonacci(num), [0])

    def test_one_fibonacci(self):
        num = 1
        self.assertEqual(main.fibonacci(num), [0, 1])

    def test_multi_fibonacci(self):
        num = 6
        self.assertEqual(main.fibonacci(num), [0, 1, 1, 2, 3, 5])

    # For fizzbuzz
    def test_fizz(self):
        num = 3
        self.assertEqual(main.fizzbuzz(num), 'Fizz')

    def test_buzz(self):
        num = 5
        self.assertEqual(main.fizzbuzz(num), 'Buzz')

    def test_fizzbuzz(self):
        num = 15
        self.assertEqual(main.fizzbuzz(num), 'FizzBuzz')


        # For find_first_non_repeating_char
    def test_find_first_non_repeating_char(self):
        self.assertEqual(main.find_first_non_repeating_char('abca'), 'b')
        self.assertEqual(main.find_first_non_repeating_char('ccbaab'), 'b')
        self.assertEqual(main.find_first_non_repeating_char('aabbcc'), '')
        self.assertEqual(main.find_first_non_repeating_char('z'), 'z')

    # For find_longest_substring_without_repeating_characters
    def test_find_longest_substring_without_repeating_characters(self):
        self.assertEqual(main.find_longest_substring_without_repeating_characters('abcabcbb'), 'abc')
        self.assertEqual(main.find_longest_substring_without_repeating_characters('bbbbb'), 'b')
        self.assertEqual(main.find_longest_substring_without_repeating_characters('pwwkew'), 'wke')
        self.assertEqual(main.find_longest_substring_without_repeating_characters(''), '')

    # For longest_substring_with_k_distinct_characters
    def test_longest_substring_with_k_distinct_characters(self):
        self.assertEqual(main.longest_substring_with_k_distinct_characters('abcabcbb', 2), 'abc')
        self.assertEqual(main.longest_substring_with_k_distinct_characters('bbbbb', 3), '')
        self.assertEqual(main.longest_substring_with_k_distinct_characters('pwwkew', 3), 'wke')
        self.assertEqual(main.longest_substring_with_k_distinct_characters('', 2), '')

    # For longest_palindromic_substring
    def test_longest_palindromic_substring(self):
        self.assertEqual(main.longest_palindromic_substring('babad'), 'bab')
        self.assertEqual(main.longest_palindromic_substring('cbbd'), 'bb')
        self.assertEqual(main.longest_palindromic_substring('a'), 'a')
        self.assertEqual(main.longest_palindromic_substring(''), '')

    # For longest_common_substring
    def test_longest_common_substring(self):
        self.assertEqual(main.longest_common_substring('abcde', 'bcde'), 'bcde')
        self.assertEqual(main.longest_common_substring('abcdef', 'abef'), 'abe')
        self.assertEqual(main.longest_common_substring('abc', ''), '')
        self.assertEqual(main.longest_common_substring('', 'abc'), '')

if __name__ == '__main__':
    unittest.main()
