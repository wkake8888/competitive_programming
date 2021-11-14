import unittest
from work_test import check_palindrome

class TestPalindrome(unittest.TestCase):

    def test_length_zero(self):
        text = ""
        self.assertEqual(check_palindrome(text), False)

    def test_length_one(self):
        text = "a"
        self.assertEqual(check_palindrome(text), True)

    def test_not_palindrome(self):
        text = "abcd"
        self.assertEqual(check_palindrome(text), False)

    def test_contain_upper(self):
        text = "Madam"
        self.assertEqual(check_palindrome(text), True)

    def test_contain_space(self):
        text = "Was it a cat I saw"
        self.assertEqual(check_palindrome(text), True)

    def test_contain_comma(self):
        text = "Eva, can I see bees in a cave"
        self.assertEqual(check_palindrome(text), True)

    def test_contain_question(self):
        text = "I did, did I?"
        self.assertEqual(check_palindrome(text), True)

    def test_contain_period(self):
        text = "Step on no pets."
        self.assertEqual(check_palindrome(text), True)

    def test_contain_exclamation_mark(self):
        text = "Sit on a potato pan, Otis!"
        self.assertEqual(check_palindrome(text), True)

    def test_contain_quatation_mark(self):
        text = "Don't nod"
        self.assertEqual(check_palindrome(text), True)

if __name__ == '__main__':
    unittest.main()
