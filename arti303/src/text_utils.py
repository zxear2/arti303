"""Text cleaning utility functions."""


def clean_name(raw):
    """Clean and format a raw student name string."""
    cleaned = " ".join(raw.split())
    return cleaned.title()
