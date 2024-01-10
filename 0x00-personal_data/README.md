# personal data
## Obfuscating Log Messages
To protect the privacy of individuals, it is important to obfuscate log messages that contain
personal information. The following examples demonstrate how you can achieve this:
```python
import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscate specified fields in a log message."""
    return re.sub(
        r'(' + '|'.join(fields) + r')=[^{}]*'.format(
            separator), lambda m: m.group(1) + '=' + redaction, message)
```
Usage:
```python
└─$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))

└─$ ./main.py
name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;
```

## Password Encryption

Password hashing using the bcrypt algorithm and how to check if a plaintext password matches a stored hashed password.

**bcrypt**

bcrypt is a password hashing function designed to be slow and difficult to brute-force. It uses a combination of a salt and a hashing algorithm to generate a unique hash for each password.

**Hashing a Password**

To hash a password, we use the `hash_password` function. This function takes a plaintext password as input and returns a hashed password as output.

```python
def hash_password(password: str) -> bytes:
    """Hash a password using the bcrypt algorithm."""
    salt = bcrypt.gensalt()  # Generate a random salt
    return bcrypt.hashpw(password.encode('utf-8'), salt)
```

**Checking a Password**

To check if a plaintext password matches a stored hashed password, we use the `is_valid` function. This function takes a hashed password and a plaintext password as input and returns a boolean value indicating whether the passwords match.

```python
def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if a plaintext password matches a stored hashed password."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
```

**Usage**

To use this code, you can import the `hash_password` and `is_valid` functions into your own code. You can then use the `hash_password` function to hash passwords and the `is_valid` function to check if passwords match.

For example, the following code shows how to hash a password and then check if a plaintext password matches the hashed password:

```python
from password_encryption import hash_password, is_valid

password = b"my_password"
encrypted_password = hash_password(password)
is_valid(encrypted_password, password)