import os
import shutil
import time

def get_all_files(directory):
    """
    Recursively get all files in the directory and subdirectories.
    """
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def should_copy(src, dest):
    """
    Determine if the file should be copied based on modification times.
    """
    if not os.path.exists(dest):
        return True
    return os.path.getmtime(src) > os.path.getmtime(dest)

def synchronize_directories(src_dir, dest_dir):
    """
    Synchronize the contents of src_dir with dest_dir.
    """
    # Get all source files
    src_files = get_all_files(src_dir)
    
    for src_file in src_files:
        # Construct destination file path
        relative_path = os.path.relpath(src_file, src_dir)
        dest_file = os.path.join(dest_dir, relative_path)
        
        # Ensure destination directory exists
        dest_file_dir = os.path.dirname(dest_file)
        os.makedirs(dest_file_dir, exist_ok=True)
        
        # Copy file if needed
        if should_copy(src_file, dest_file):
            print(f'Copying {src_file} to {dest_file}')
            shutil.copy2(src_file, dest_file)
    
    # Remove files in destination that are not in source
    dest_files = get_all_files(dest_dir)
    for dest_file in dest_files:
        relative_path = os.path.relpath(dest_file, dest_dir)
        src_file = os.path.join(src_dir, relative_path)
        if not os.path.exists(src_file):
            print(f'Removing {dest_file}')
            os.remove(dest_file)

def main():
    # Define source and destination directories
    src_dir = 'path/to/source'
    dest_dir = 'path/to/destination'

    # Ensure destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Synchronize directories
    synchronize_directories(src_dir, dest_dir)

if __name__ == "__main__":
    main()
