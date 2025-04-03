README
Overview
This repository contains several notebooks that perform analyses and generate figures using JSON data along with other datasets. Each notebook includes all the code used to generate the figures, so you can both inspect the code and reproduce the results.

Running the Notebooks
File Path Configuration:
The notebooks have been updated to automatically locate JSON files in the Jsons/ directory and .mat files in the Data/Nmatchstim/ directory.

Data Files:
- JSON files are already included in the Jsons/ directory
- .mat files need to be downloaded to the Data/Nmatchstim/ directory (see instructions below)

All figures are already generated and are included in the notebooks along with the corresponding code. Note that running the entire notebook may take a while due to the computationally intensive permutation analyses involved.
Downloading .mat Files:

1. run download_data.py file 

or 

2. Download the file from https://drive.google.com/file/d/17GhaISng0Bh6V7WNidmrz0QVqZeee89Z/view?usp=drive_link

Extracting .mat Files:

1. Automatic extraction when running notebooks:
   - The first cell of each notebook will automatically extract the .mat files from the zip
   
2. Using the extraction script:
   - Run the script: python extract_mat_files.py
   - The script will extract all .mat files to the Data/Nmatchstim/ directory
Alternatively, you can manually extract the .mat files from the zip and place them in the Data/Nmatchstim/ directory.

GPU Acceleration:
The notebooks are set up to use GPU acceleration via PyTorch when a compatible GPU is available. Ensure that your PyTorch installation supports CUDA and that you have a GPU enabled in your environment. If a GPU is detected, the notebooks will automatically leverage it for faster computation. On a CPU-only system, the notebooks will still run, but performance may be slower.

Dependencies
Make sure to install the required libraries (e.g., NumPy, Matplotlib, PyTorch, scikit-learn, Pandas, etc.) before running the notebooks on your own computer. Additionally, the download script requires the 'gdown' package to download files from Google Drive.

You can install all dependencies with:
```
pip install numpy matplotlib torch scikit-learn pandas
```

Alternatively, you can run the notebooks in a Google Colab environment, which comes preloaded with required libraries and provides free GPU access.

Contact
If you encounter any issues, feel free to reach out at:

umuryildiz_@outlook.com
umur.yildiz@ug.bilkent.edu.tr