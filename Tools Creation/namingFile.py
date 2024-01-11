import os

directory_path = r'U:\Atit\Coding\AI\CustomData\Revolution-Bytes\Images'

if not os.path.exists(directory_path):
    print(f"Directory '{directory_path}' does not exist.")
    exit()

# List all files and sort
file_list = os.listdir(directory_path)
file_list.sort()

num_images = len(file_list)

# rename
for count, old_name in enumerate(file_list, start=1):

    new_name = f"{count}"
    new_path = os.path.join(directory_path, f"{new_name}.jpg")
    old_path = os.path.join(directory_path, old_name)
    
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}.jpg")
    else:
        print(f"File not found: {old_path}")

print(f"Successfully renamed {num_images} images.")
