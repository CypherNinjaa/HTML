import os
import pyzipper  # Install using: pip install pyzipper
from collections import defaultdict

# Define the directory where the files are located
directory = r'C:\Users\vikas\Downloads\Telegram Desktop'  # Change this to your directory

# Password for the ZIP files
zip_password = b"@cypherninjaa"  # Must be in bytes

# Initialize a defaultdict to group files by their starting numbers
file_groups = defaultdict(list)

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if (filename.endswith('.mp4') or filename.endswith('.pdf')) and filename[:2].isdigit():
        # Get the starting number from the filename (e.g., '01', '02', etc.)
        group_key = filename[:2]
        file_path = os.path.join(directory, filename)
        
        # Group files by their starting number
        file_groups[group_key].append(file_path)

# Create a password-protected zip file for each group
for group_key, files in file_groups.items():
    # Define the zip file name based on the group number
    zip_file_name = os.path.join(directory, f"{group_key}_@cypherninjaa.zip")
    
    # Create a password-protected zip file
    with pyzipper.AESZipFile(zip_file_name, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
        zipf.setpassword(zip_password)  # Set the password
        for file in files:
            zipf.write(file, os.path.basename(file))  # Add file to the zip (preserve filename)
    
    print(f"Created password-protected zip file: {zip_file_name}")

print("✅ Zipping complete with password protection!")
