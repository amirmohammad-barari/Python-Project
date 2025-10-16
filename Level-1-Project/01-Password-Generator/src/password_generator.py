import random, string
from typing import List, Optional
from abc import ABC, abstractmethod
from nltk.corpus import words


class PasswordGenerator(ABC):
    """Abstract base class for all password generators."""

    @abstractmethod
    def generate_password(self) -> str:
        """
        Generate a password string.

        Returns:
            str: The generated password.
        """
        pass


class PincodeGenerator(PasswordGenerator):
    """Generates numeric PIN codes of a given length."""

    def __init__(self, length: int = 8):
        """
        Initialize the PIN code generator.

        Args:
            length (int, optional): Length of the generated PIN code. Defaults to 8.
        """
        self.length = length

    def generate_password(self) -> str:
        """
        Generate a numeric PIN code of the specified length.

        Returns:
            str: The generated PIN code containing only digits.
        """
        return "".join(str(random.randint(0, 9)) for _ in range(self.length))


class RandomPasswordGenerator(PasswordGenerator):
    """Generates random passwords using letters, symbols, and digits."""

    def __init__(self, length: int = 8, include_symbol: bool = True, include_number: bool = True):
        """
        Initialize the random password generator.

        Args:
            length (int, optional): Desired password length. Defaults to 8.
            include_symbol (bool, optional): Whether to include punctuation symbols. Defaults to True.
            include_number (bool, optional): Whether to include digits. Defaults to True.
        """
        self.length = length
        self.char = string.ascii_letters
        if include_symbol:
            self.char += string.punctuation
        if include_number:
            self.char += string.digits

    def generate_password(self) -> str:
        """
        Generate a random password containing letters, symbols, and digits.

        Returns:
            str: The generated random password.
        """
        return "".join(random.choice(self.char) for _ in range(self.length))


class MemorablePasswordGenerator(PasswordGenerator):
    """Generates readable, human-friendly passwords based on real words."""

    def __init__(
        self,
        word_count: int = 3,
        separator: str = "-",
        capitalize: bool = False,
        vocabulary: Optional[List[str]] = None
    ):
        """
        Initialize the memorable password generator.

        Args:
            word_count (int, optional): Number of words to include. Defaults to 3.
            separator (str, optional): Separator between words. Defaults to "-".
            capitalize (bool, optional): Whether to capitalize each word. Defaults to False.
            vocabulary (List[str], optional): Custom vocabulary list. Defaults to nltk.corpus.words.
        """
        if vocabulary is None:
            vocabulary = words.words()

        self.word_count = word_count
        self.separator = separator
        self.capitalize = capitalize
        self.vocabulary: List[str] = vocabulary

    def generate_password(self) -> str:
        """
        Generate a human-readable password composed of real words.

        Returns:
            str: The generated memorable password.
        """
        chosen = [random.choice(self.vocabulary) for _ in range(self.word_count)]
        if self.capitalize:
            chosen = [w.capitalize() for w in chosen]
        return self.separator.join(chosen)


def test_pincode():
    """
    Test the PincodeGenerator for correct length and numeric-only output.
    """
    pincode_gen = PincodeGenerator(length=8)
    pin = pincode_gen.generate_password()
    assert len(pin) == 8
    assert all(char in string.digits for char in pin)
    print(f"Pincode: {pin}")


def test_random_password():
    """
    Test the RandomPasswordGenerator for symbol and digit inclusion.
    """
    random_gen = RandomPasswordGenerator(length=12, include_symbol=True, include_number=True)
    password = random_gen.generate_password()
    assert len(password) == 12
    assert any(char in string.punctuation for char in password)
    assert any(char in string.digits for char in password)
    print(f"Random Password: {password}")


def test_memorable_password():
    """
    Test the MemorablePasswordGenerator for correct word count and capitalization.
    """
    memorable_gen = MemorablePasswordGenerator(word_count=4, separator="_", capitalize=True)
    memorable_password = memorable_gen.generate_password()
    assert len(memorable_password.split("_")) == 4
    assert all(word[0].isupper() for word in memorable_password.split("_"))
    print(f"Memorable Password: {memorable_password}")


def main():
    """
    Run tests for all password generator classes.
    """
    print("Test Pincode Generator")
    test_pincode()
    print("Test Random Password Generator")
    test_random_password()
    print("Test Memorable Password Generator")
    test_memorable_password()


if __name__ == "__main__":
    main()
