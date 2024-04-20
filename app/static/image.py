import os

def rename_files(folder_path, extension='.jpg'):
    # Get list of files in the specified folder
    files = os.listdir(folder_path)
    
    # Filter out non-image files based on the file extension
    image_files = [file for file in files if file.endswith(extension)]
    
    # Sort the image files to ensure consistent naming order
    image_files.sort()
    
    # Rename each image file sequentially
    for index, old_name in enumerate(image_files):
        # Define the new file name with the desired format (e.g., image1.jpg, image2.jpg, etc.)
        new_name = f'image{index + 1}{extension}'
        
        # Construct the full paths for old and new file names
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        
        try:
            # Rename the file by moving it to the new path
            os.rename(old_path, new_path)
            print(f'Renamed: {old_name} -> {new_name}')
        except OSError as e:
            print(f'Error renaming {old_name}: {e}')

# Example usage:
base_dir = os.path.abspath(os.path.dirname(__file__))

folder_path = "/Users/charley/CS2270/coolness_factor/app/static/images/"
print(folder_path)
print(os.getcwd())

rename_files(folder_path)
