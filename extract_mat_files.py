import os
import zipfile
import glob

def extract_mat_files():
    """Extract .mat files from zip archives in the Data directory"""
    # Create the Data/Nmatchstim directory if it doesn't exist
    os.makedirs("Data/Nmatchstim", exist_ok=True)
    
    # Look for zip files in the Data directory
    zip_files = glob.glob("Data/Nmatchstim/*.zip")
    
    if not zip_files:
        print("No zip files found in the Data directory.")
        print("Please make sure you have placed the zip file containing .mat files in the Data/ directory.")
        return False
    
    extracted_count = 0
    for zip_path in zip_files:
        print(f"Found zip file: {zip_path}")
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                # List all files in the zip
                file_list = zip_ref.namelist()
                mat_files = [f for f in file_list if f.endswith('.mat')]
                
                if not mat_files:
                    print(f"No .mat files found in {zip_path}")
                    continue
                
                print(f"Found {len(mat_files)} .mat files in the zip. Extracting...")
                
                # Extract only .mat files to the Nmatchstim directory
                for mat_file in mat_files:
                    # Get just the filename without any directory structure
                    filename = os.path.basename(mat_file)
                    target_path = os.path.join("Data", "Nmatchstim", filename)
                    
                    # Skip if file already exists
                    if os.path.exists(target_path):
                        print(f"File {filename} already exists, skipping.")
                        continue
                    
                    # Extract the file
                    print(f"Extracting {filename}...")
                    with zip_ref.open(mat_file) as source:
                        with open(target_path, 'wb') as target:
                            target.write(source.read())
                    
                    extracted_count += 1
                    print(f"Successfully extracted {filename}")
                    
        except zipfile.BadZipFile:
            print(f"Error: {zip_path} is not a valid zip file.")
        except Exception as e:
            print(f"Error extracting from {zip_path}: {e}")
    
    if extracted_count > 0:
        print(f"\nSuccessfully extracted {extracted_count} .mat files to Data/Nmatchstim/")
        return True
    else:
        print("\nNo new .mat files were extracted. They might already exist in the target directory.")
        return False

if __name__ == "__main__":
    extract_mat_files() 