# Q4. Automating Software Package Updates
# Write a Python program to automate the checking and updating of installed software packages on a Linux server. The script should:
# Function to check for available updates using the system’s package manager (e.g., apt, yum). and list all available updates.
# Ask user to Update all at once or provide any specific package name to update (take package index number for ease)
# Install the available updates based on user input.
# If any updates fail to install, log the error and send an alert (e.g., console log).
# Optionally, schedule the script to run at a certain cron.

import os
import subprocess

def check_updates():
    """Checks for available updates and lists them."""
    try:
        result = subprocess.run(["sudo", "apt", "list", "--upgradable"], capture_output=True, text=True, check=True)
        updates = result.stdout.split('\n')[1:-1]  # Remove headers and empty lines
        return updates
    except subprocess.CalledProcessError as e:
        print("Error checking updates:", e)
        return []

def install_update(package_name):
    """Installs a specific package update."""
    try:
        subprocess.run(["sudo", "apt", "install", "-y", package_name], check=True)
        print(f"{package_name} updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to update {package_name}: {e}")

def install_all_updates():
    """Installs all available updates."""
    try:
        subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
        print("All packages updated successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to update all packages:", e)

def main():
    updates = check_updates()
    
    if not updates:
        print("No updates available.")
        return
    
    print("Available updates:")
    for i, update in enumerate(updates, start=1):
        print(f"{i}. {update.split('/')[0]}")
    
    choice = input("Do you want to update all packages (a) or a specific one (enter number)? ").strip().lower()
    
    if choice == 'a':
        install_all_updates()
    elif choice.isdigit() and 1 <= int(choice) <= len(updates):
        package_name = updates[int(choice) - 1].split('/')[0]
        install_update(package_name)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()