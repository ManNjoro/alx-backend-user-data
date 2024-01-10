#!/usr/bin/env python3
"""
Script that obfuscates the log message
"""

import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscate specified fields in a log message."""
    return re.sub(
        r'(' + '|'.join(fields) + r')=[^{}]*'.format(
            separator), lambda m: m.group(1) + '=' + redaction, message)
