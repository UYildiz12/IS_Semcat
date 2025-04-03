#!/usr/bin/env python3
import os
import sys
import subprocess

# Ensure gdown is installed
try:
    import gdown
except ImportError:
    print("gdown not found. Installing gdown...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "gdown"])
    import gdown

def download_data():
    # Google Drive file URL (converted to a direct download link)
    url = "https://drive.google.com/uc?export=download&id=17GhaISng0Bh6V7WNidmrz0QVqZeee89Z"
    
    # Define the target directory (data/nmatchstim)
    target_dir = os.path.join("data", "nmatchstim")
    
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)
        print(f"Created directory: {target_dir}")
    else:
        print(f"Directory already exists: {target_dir}")
    
    # Define the output file path (adjust the filename if necessary)
    output_file = os.path.join(target_dir, "stims.zip")
    
    # Download the file
    print("Downloading file from Google Drive...")
    gdown.download(url, output_file, quiet=False)
    print("Download completed.")

if __name__ == "__main__":
    download_data()
