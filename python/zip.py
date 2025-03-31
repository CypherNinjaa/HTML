import os
import zipfile
from collections import defaultdict

# Define the directory where the files are located
directory = r'C:\Users\vikas\Downloads\Telegram Desktop'  # Change this to your directory

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

# Create a zip file for each group of files
for group_key, files in file_groups.items():
    # Define the zip file name based on the group number
    zip_file_name = os.path.join(directory, f"{group_key}_@cypherninjaa.zip")
    
    # Create a zip file and add all files in the group
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))  # Add file to the zip (preserve the filename)
    
    print(f"Created zip file: {zip_file_name}")

print("Zipping complete.")
