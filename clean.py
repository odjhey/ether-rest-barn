from pathlib import Path

directory_path = "./outs" # Replace with your directory's path

p = Path(directory_path)
for file_path in p.glob("*.png"):
    if file_path.is_file():
        file_path.unlink() # Deletes the file
        print(f"Deleted: {file_path}")
