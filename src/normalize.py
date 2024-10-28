import re

def normalize_name(name):
    """Normalize the name by removing special characters and spaces."""
    return re.sub(r'\W+', '_', name).lower()