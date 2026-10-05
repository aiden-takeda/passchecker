import string
import unittest

from password_checker import (
    validate_password,
    validate_password_with_error_messages,
    validate_password_with_error_messages_regex,
)


class TestValidatePassword(unittest.TestCase):
    def test_password_length(self):
        assert validate_password("sh0rt_") == False
        assert validate_password("v3ry_very_long_String") == False

    def test_password_uppercase(self):
        assert validate_password("test-passw0rd") == False

    def test_password_lowercase(self):
        assert validate_password("T3ST_PASSWORD") == False

    def test_password_digit(self):
        assert validate_password("Test_password") == False

    def test_password_special_character(self):
        assert validate_password("Password1") == False

    def test_password_valid(self):
        assert validate_password("New_123123") == True


class TestValidatePasswordWithErrorMessages(unittest.TestCase):
    def test_valid_passwords_at_length_boundaries(self):
        for password in ("Abcdef1!", "Abcdefghijklmnopqr1!"):
            with self.subTest(password=password):
                self.assertIsNone(validate_password_with_error_messages(password))

    def test_invalid_passwords_raise_the_first_matching_message(self):
        cases = (
            ("Aa1!", "Password must be between 8 and 20 characters long."),
            ("Abcdefghijklmnopqr1!x", "Password must be between 8 and 20 characters long."),
            ("Abcdefg!", "Password must contain at least one digit."),
            ("abcdef1!", "Password must contain at least one uppercase letter."),
            ("ABCDEF1!", "Password must contain at least one lowercase letter."),
            ("Abcdef12", "Password must contain at least one special character."),
        )

        for password, message in cases:
            with self.subTest(password=password):
                with self.assertRaises(ValueError) as raised:
                    validate_password_with_error_messages(password)
                self.assertEqual(str(raised.exception), message)


if __name__ == "__main__":
    unittest.main()
