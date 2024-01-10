#!/usr/bin/env python3
"""
Script that obfuscates the log message
"""

from typing import List
import logging
import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscate specified fields in a log message."""
    return re.sub(
        r'(' + '|'.join(fields) + r')=[^{}]*'.format(
            separator), lambda m: m.group(1) + '=' + redaction, message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the RedactingFormatter."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record."""
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)
