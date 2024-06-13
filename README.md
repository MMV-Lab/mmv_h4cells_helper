# mmv_h4cells_helper

This repository contains supplementary scripts for preparing data for the [MMV_H4Cells](https://github.com/MMV-Lab/mmv_h4cells) napari plugin. For more information, read the corresponding [README](https://github.com/MMV-Lab/mmv_h4cells/blob/main/README.md).

## Installation

1. **Set up the environment**:

    - Install [Anaconda](https://www.anaconda.com/download/success). 
        - If you've never heard of Anaconda, [this](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) or [this](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf) might be helpful.
    - Use the Anaconda Prompt to clone this repository to your local machine:
        ```bash
        git clone https://github.com/MMV-Lab/mmv_h4cells_helper.git
        ```

        If you don't have Git installed, you can alternatively download the repository as a ZIP file. Click on the green "Code" button at the top of the repository page, select "Download ZIP", and then unzip the downloaded file.

    - Navigate to the cloned repository:
        Use the Anaconda Prompt to navigate to the directory where you have cloned or unzipped this repository.
        ```bash
        cd mmv_h4cells_helper
        ```

    - Create a new environment:
        ```bash
        conda create --name mmv_h4cells_helper python=3.9
        conda activate mmv_h4cells_helper
        ```

2. **Install the required dependencies**:

    - Install `cellpose` and `aicsimageio` via `pip`:
        ```bash
        pip install cellpose aicsimageio
        ```

    - If you encounter any issues with the installation, you can alternatively use the `requirements.txt` file:
        ```bash
        pip install -r requirements.txt
        ```
        In this case, you might need to create a new environment as described above.

3. **Optional: GPU support**:
    If you wish to use GPU for faster computation, follow the instructions provided [here](https://github.com/MouseLand/cellpose?tab=readme-ov-file#gpu-version-cuda-on-windows-or-linux) to install the GPU version of the required libraries.


## Usage

An example data file (`data\raw\sample.tif`) in the `data` directory can be used to run the scripts and understand the workflow. To execute the scripts, follow these steps:

1. **Change to the directory containing the scripts**:
    Make sure to adjust the path to the directory where you have cloned this repository.
    ```bash
    cd \User\Desktop\mmv_h4cells_helper
    ```

2. **Segment the cells and cell nuclei**:

    - To segment the cells, run:
        ```bash
        python inference_cells.py
        ```

    - To segment the cell nuclei, run:
        ```bash
        python inference_nuclei.py
        ```

3. **Match the masks**:

    - To generate a mask containing only the cells with at least one completely contained nucleus, run:
        ```bash
        python get_double_positives.py
        ```
    - The mask will be exported to the `results` folder and can be opened and further processed using napari and the `MMV_H4Cells` plugin.


4. **Custom Data**:

    - To process your own `.tif` files, simply place them in the `data/raw/` directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.