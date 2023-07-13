import os
import shutil

# Specify the source directory containing the PDF files
source_directory = r"C:/Users/leevo/OneDrive/Documents/scrapper/filerename/schneider"

# Specify the destination directory where the copied files will be stored
destination_directory = r"C:/Users/leevo/OneDrive/Documents/scrapper/filerename/schneiderRenamed"

# Loop through the source directory
for filename in os.listdir(source_directory):
    if filename.endswith(".pdf"):
        # Extract the new file name
        new_file_name = filename.split("_")[1].split(".")[0]
        
        # Specify the path for the new copied file
        new_file_path = os.path.join(destination_directory, new_file_name + ".pdf")
        
        # Copy and rename the file
        shutil.copy2(os.path.join(source_directory, filename), new_file_path)
        
        print("File copied and renamed to:", new_file_path)
