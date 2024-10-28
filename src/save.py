import os
from .normalize import normalize_name

def save_file(output_file):
    """Normalizes the file name and ensures the output directory exists."""
    output_dir = "../done"
    
    output_extension = output_file.split('.')[-1].lower()
    
    normalized_file_name = normalize_name(output_file.rsplit('.', 1)[0])
    
    full_output_path = os.path.join(output_dir, f"{normalized_file_name}.{output_extension}")
    
    os.makedirs(output_dir, exist_ok=True)
    
    return full_output_path
