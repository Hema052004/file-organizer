import os
import shutil

def organize_by_extension(folder_path):
    """
    For every file in folder_path (not subfolders), create (if needed)
    a subfolder named after its extension (uppercase, no dot), then move it.
    """
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        # Skip if this is a directory
        if os.path.isdir(full_path):
            continue

        # Split filename into base and extension
        name, ext = os.path.splitext(filename)
        if not ext:
            ext_folder = "NoExtension"
        else:
            ext_folder = ext[1:].upper()  # ".pdf" → "PDF"

        # Ensure the destination folder exists
        dest_dir = os.path.join(folder_path, ext_folder)
        os.makedirs(dest_dir, exist_ok=True)

        # Move the file into the folder
        dest_path = os.path.join(dest_dir, filename)
        shutil.move(full_path, dest_path)
        print(f"Moved {filename} → {ext_folder}/")

if __name__ == "__main__":
    path = input("Enter the full folder path you want to organize:\n").strip()
    organize_by_extension(path)
    print("Organization complete.")
