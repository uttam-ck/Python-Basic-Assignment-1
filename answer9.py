# Q9. File Version Control System
# Write a Python program to simulate a basic version control system for a directory of files. The script should:
# Accept a directory path as input and store versions of files whenever changes are made.
# Each time a file is modified, the script should create a new version and save it in a separate folder (e.g., ./versions).
# Keep track of file versions by naming them with a version number or timestamp (e.g., file_v1.txt, file_v2.txt).
# When a file is restored to a previous version, it should be copied from the version folder back to the original directory.
# Bonus:
# Implement the ability to compare file versions and show differences (similar to diff).
# Add an option to automatically clean up old versions, keeping only the last n versions of each file.

import os
import shutil
import hashlib
import time

def get_file_checksum(file_path):
    """Generates a checksum for file content."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def save_version(file_path, versions_dir):
    """Saves a new version of a file if changes are detected."""
    file_name = os.path.basename(file_path)
    file_version_dir = os.path.join(versions_dir, file_name)
    os.makedirs(file_version_dir, exist_ok=True)
    
    version_number = len(os.listdir(file_version_dir)) + 1
    version_file = os.path.join(file_version_dir, f"{file_name}_v{version_number}.txt")
    shutil.copy2(file_path, version_file)
    print(f"Saved version {version_number} for {file_name}")

def track_changes(directory, versions_dir):
    """Monitors files in a directory and saves versions when changes occur."""
    file_checksums = {}
    while True:
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):
                checksum = get_file_checksum(file_path)
                if file_name not in file_checksums or file_checksums[file_name] != checksum:
                    save_version(file_path, versions_dir)
                    file_checksums[file_name] = checksum
        time.sleep(10)  # Check for changes every 10 seconds

def restore_version(file_name, version_number, versions_dir, target_dir):
    """Restores a specific version of a file back to the target directory."""
    version_path = os.path.join(versions_dir, file_name, f"{file_name}_v{version_number}.txt")
    if os.path.exists(version_path):
        shutil.copy2(version_path, os.path.join(target_dir, file_name))
        print(f"Restored {file_name} to version {version_number}")
    else:
        print(f"Version {version_number} not found for {file_name}")

if __name__ == "__main__":
    directory = "./watched_files"
    versions_directory = "./versions"
    os.makedirs(directory, exist_ok=True)
    os.makedirs(versions_directory, exist_ok=True)
    print("Tracking changes in", directory)
    track_changes(directory, versions_directory)
