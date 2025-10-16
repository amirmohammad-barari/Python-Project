# 🔐 Password Generator Library

A modular, object-oriented Python library for generating different types of passwords — from simple numeric PIN codes to strong random or memorable word-based passwords.

---

## 🧩 Overview

This library provides three main password generator classes, each inheriting from a common abstract base class `PasswordGenerator`:

| Class | Description |
|-------|--------------|
| `PincodeGenerator` | Generates numeric PIN codes (e.g., `48392015`) |
| `RandomPasswordGenerator` | Generates random passwords with letters, digits, and symbols (e.g., `p@X9r#G1z$Qf`) |
| `MemorablePasswordGenerator` | Generates readable passwords composed of real words (e.g., `River-Apple-Cloud`) |

---

## 🏗️ Project Structure

```
password_generator/
│
├── src/
│   └── password_generator.py     # main source code
│
├── README.md                     # project documentation
└── requirements.txt              # dependencies (optional)
```

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/password-generator.git
   cd password-generator
   ```

2. **Install dependencies**
   ```bash
   pip install nltk
   ```

   Then download the English words list (used by `MemorablePasswordGenerator`):
   ```python
   import nltk
   nltk.download('words')
   ```

---

## 🚀 Usage

### 1. Pincode Generator
```python
from password_generator import PincodeGenerator

pincode = PincodeGenerator(length=6)
print(pincode.generate_password())  # e.g. "483920"
```

### 2. Random Password Generator
```python
from password_generator import RandomPasswordGenerator

generator = RandomPasswordGenerator(length=12, include_symbol=True, include_number=True)
print(generator.generate_password())  # e.g. "p@X9r#G1z$Qf"
```

### 3. Memorable Password Generator
```python
from password_generator import MemorablePasswordGenerator

memorable = MemorablePasswordGenerator(word_count=4, separator="-", capitalize=True)
print(memorable.generate_password())  # e.g. "River-Apple-Cloud-Sun"
```

---

## 🧪 Running Tests

You can quickly test all password generators by running the file directly:

```bash
python password_generator.py
```

Sample output:
```
Test Pincode Generator
Pincode: 93847210
Test Random Password Generator
Random Password: aP@4qK#xG9!s
Test Memorable Password Generator
Memorable Password: Tree_Moon_River_Stone
```

---

## 🔒 Security Note

- For production or cryptographic use, consider replacing `random` with the `secrets` module for stronger randomness.
- Example:
  ```python
  import secrets
  secrets.choice(string.ascii_letters)
  ```

---

## 🧰 Features

- Abstract and extensible design (`PasswordGenerator` base class)
- Fully type-annotated and documented (PEP-257 compliant)
- Compatible with unit testing frameworks like `pytest`
- Easy to customize (e.g., provide custom vocabularies or separators)
- No external dependencies except `nltk` (optional)

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it.

---

## ✨ Author

**Developed by:** [Amirmohammad Barari]  
**Version:** 1.0  
**Language:** Python 3.9+

---

> _“Security is not a product, but a process.”_ – Bruce Schneier
