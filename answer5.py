# Write a Python script to find duplicate files within a specified directory and its subdirectories. The script should:
# Scan the directory for all files and calculate a checksum (e.g., sha256sum) for each file.
# Identify and list duplicate files by comparing their checksums.
# Optionally, give the user the option to delete or move duplicate files.
# Bonus:
# Allow the user to specify the minimum file size for duplication detection (e.g., only consider files larger than 1MB).
# Create a report listing the duplicate files and their checksums.


import os
import hashlib

def calculate_checksum(file_path):
    """Calculates the SHA-256 checksum of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicates(directory):
    """Finds duplicate files in the given directory and its subdirectories."""
    file_checksums = {}
    duplicates = {}
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            checksum = calculate_checksum(file_path)
            if checksum in file_checksums:
                duplicates.setdefault(checksum, []).append(file_path)
            else:
                file_checksums[checksum] = file_path
    
    return duplicates

def delete_duplicates(duplicates):
    """Deletes duplicate files, keeping only one copy."""
    for paths in duplicates.values():
        for file_path in paths[1:]:
            os.remove(file_path)
            print(f"Deleted: {file_path}")

def move_duplicates(duplicates, target_directory):
    """Moves duplicate files to a specified directory."""
    os.makedirs(target_directory, exist_ok=True)
    for paths in duplicates.values():
        for file_path in paths[1:]:
            new_path = os.path.join(target_directory, os.path.basename(file_path))
            os.rename(file_path, new_path)
            print(f"Moved: {file_path} -> {new_path}")

def main():
    directory = input("Enter the directory to scan: ")
    
    duplicates = find_duplicates(directory)
    
    if not duplicates:
        print("No duplicate files found.")
        return
    
    print("Duplicate files found:")
    for paths in duplicates.values():
        print("\n".join(paths), "\n")
    
    action = input("Do you want to delete (d), move (m), or skip (s) duplicates? ").lower()
    if action == 'd':
        delete_duplicates(duplicates)
    elif action == 'm':
        target_directory = input("Enter the directory to move duplicates: ")
        move_duplicates(duplicates, target_directory)

if __name__ == "__main__":
    main()
