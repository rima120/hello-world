"""Utilities for cleaning and formatting text values."""


def clean_name(raw):
    """Return a name with collapsed whitespace and title casing."""
    return " ".join(raw.split()).title()
