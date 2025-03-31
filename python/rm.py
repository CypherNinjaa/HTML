import os

# Directory where the files are located
directory = r'C:\Users\Vikash\Downloads\Telegram Desktop'  # Change this to your actual folder

# Text to replace or add
text_to_find = "@providerhub0"
text_to_replace_with = "@cypherninjaa"

# Iterate over each file in the directory
for filename in os.listdir(directory):
    # Check if the file is an .mp4 or .pdf
    if filename.endswith('.mp4') or filename.endswith('.pdf'):
        new_filename = filename  # Start with the current filename

        # Case 1: If filename contains "@providerhub0", replace it with "@cypherninjaa"
        if text_to_find in filename:
            new_filename = filename.replace(text_to_find, text_to_replace_with)

        # Case 2: If filename does NOT contain "@providerhub0", add "@cypherninjaa" before the extension
        else:
            base, ext = os.path.splitext(filename)  # Split filename and extension
            new_filename = f"{base} {text_to_replace_with}{ext}"  # Add @cypherninjaa before extension

        # Get the full paths for old and new filenames
        old_file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(directory, new_filename)

        # Rename the file only if the name has changed
        if old_file_path != new_file_path:
            try:
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {filename} -> {new_filename}")
            except Exception as e:
                print(f"Error renaming {filename}: {e}")

print("✅ Renaming complete!")
