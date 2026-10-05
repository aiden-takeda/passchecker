import re
import string


def validate_password(password: str) -> bool:
    """Return True when the password matches the required policy.

    The policy requires a length between 8 and 20 characters, at least one
    digit, one uppercase letter, one lowercase letter, and one punctuation
    character.

    Args:
        password: The candidate password to validate.

    Returns:
        True if the password satisfies all validation rules; otherwise False.
    """
    if len(password) < 8 or len(password) > 20:
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char in string.punctuation for char in password):
        return False

    return True


def validate_password_with_error_messages(password: str) -> None:
    """Validate a password and raise a clear ValueError for the first rule failure.

    The password must:
    - be between 8 and 20 characters long,
    - include at least one digit,
    - include at least one uppercase letter,
    - include at least one lowercase letter,
    - include at least one punctuation character.

    Args:
        password: The password to validate.

    Raises:
        ValueError: If the password fails any validation rule.
    """
    if len(password) < 8 or len(password) > 20:
        raise ValueError("Password must be between 8 and 20 characters long.")

    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit.")

    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase letter.")

    if not any(char.islower() for char in password):
        raise ValueError("Password must contain at least one lowercase letter.")

    if not any(char in string.punctuation for char in password):
        raise ValueError("Password must contain at least one special character.")


def validate_password_with_error_messages_regex(password: str) -> None:
    """Validate a password using regular expressions and raise a clear error.

    This function enforces the same rules as the other validators: the password
    must be 8 to 20 characters long, and contain at least one digit, uppercase
    letter, lowercase letter, and special character.

    Args:
        password: The password to validate.

    Raises:
        ValueError: If the password fails any required rule.
    """
    if not re.fullmatch(r".{8,20}", password):
        raise ValueError("Password must be between 8 and 20 characters long.")

    if not re.search(r"\d", password):
        raise ValueError("Password must contain at least one digit.")

    if not re.search(r"[A-Z]", password):
        raise ValueError("Password must contain at least one uppercase letter.")

    if not re.search(r"[a-z]", password):
        raise ValueError("Password must contain at least one lowercase letter.")

    if not re.search(r"[!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~]", password):
        raise ValueError("Password must contain at least one special character.")
