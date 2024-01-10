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
