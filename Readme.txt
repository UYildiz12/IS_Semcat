README
Overview
This repository contains several notebooks that perform analyses and generate figures using JSON data along with other datasets. Each notebook includes all the code used to generate the figures, so you can both inspect the code and reproduce the results.

Running the Notebooks
File Path Configuration:
To run the notebooks, update the file paths for the JSON files match the file paths in the scripts.

All figures are already generated and are included in the notebooks along with the corresponding code. Note that running the entire notebook may take a while due to the computationally intensive permutation analyses involved.

GPU Acceleration:
The notebooks are set up to use GPU acceleration via PyTorch when a compatible GPU is available. Ensure that your PyTorch installation supports CUDA and that you have a GPU enabled in your environment. If a GPU is detected, the notebooks will automatically leverage it for faster computation. On a CPU-only system, the notebooks will still run, but performance may be slower.

Dependencies
Make sure to install the required libraries (e.g., NumPy, Matplotlib, PyTorch, scikit-learn, Pandas, etc.) before running the notebooks on your own computer. Alternatively, you can run the notebooks in a Google Colab environment, which comes preloaded with required libraries and provides free GPU access.

Contact
If you encounter any issues, feel free to reach out at:

umuryildiz_@outlook.com
umur.yildiz@ug.bilkent.edu.tr