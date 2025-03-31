import os

# Directory where the files are located
directory = r'C:\Users\vikas\Downloads\Telegram Desktop'  # Change this to your actual folder

# Iterate over each file in the directory
for filename in os.listdir(directory):
    # Check if the file is an .mp4 or .pdf
    if filename.endswith('.mp4') or filename.endswith('.pdf'):
        file_path = os.path.join(directory, filename)
        
        try:
            os.remove(file_path)  # Delete the file
            print(f"Deleted: {filename}")
        except Exception as e:
            print(f"Error deleting {filename}: {e}")

print("✅ Deletion complete!")
