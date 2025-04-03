# README

## Overview

This repository contains several notebooks that perform analyses and generate figures using JSON data along with other datasets. Each notebook includes all the code used to generate the figures, so you can inspect the code and reproduce the results.

---

## Running the Notebooks

### File Path Configuration

The notebooks have been updated to automatically locate:

- JSON files in the `Jsons/` directory  
- `.mat` files in the `Data/Nmatchstim/` directory

---

### Data Files

- ✅ **JSON files** are already included in the `Jsons/` directory  
- ❗ **.mat files** need to be downloaded to the `Data/Nmatchstim/` directory (see below)

All figures are already generated and embedded in the notebooks alongside the corresponding code.  
**Note:** Running the full notebook may take a while due to computationally intensive permutation analyses.

---

## Downloading `.mat` Files

You can obtain the `.mat` files using **either** of the following methods:

### Option 1: Run the download script  
```bash
python download_data.py
```

### Option 2: Download manually  
Download from the following link:  
📎 [Google Drive Link](https://drive.google.com/file/d/17GhaISng0Bh6V7WNidmrz0QVqZeee89Z/view?usp=drive_link)

---

## Extracting `.mat` Files

### Option 1: Automatic extraction

- The first cell of each notebook automatically extracts the `.mat` files from the zip.

### Option 2: Use the extraction script  
```bash
python extract_mat_files.py
```

- This will extract all `.mat` files into the `Data/Nmatchstim/` directory.

### Option 3: Manual extraction

- You can manually unzip the `.mat` files and place them in the `Data/Nmatchstim/` directory.

---

## GPU Acceleration

The notebooks are configured to use **GPU acceleration** via PyTorch if a compatible GPU is available.

- Ensure your PyTorch installation supports CUDA.
- If a GPU is detected, the notebooks will automatically use it for faster computation.
- On CPU-only systems, the notebooks will still run but may be slower.

---

## Dependencies

Install the required packages with:

```bash
pip install numpy matplotlib torch scikit-learn pandas
```

The `download_data.py` script also requires:

```bash
pip install gdown
```

Alternatively, run the notebooks on **Google Colab**, which:

- Comes pre-installed with all required libraries
- Provides **free GPU access**

---

## Contact

For issues, feedback, or questions, please contact:

📧 umuryildiz_@outlook.com  
📧 umur.yildiz@ug.bilkent.edu.tr
