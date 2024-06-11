# mmv_h4cells_helper

This repository contains supplementary scripts for preparing data for the [MMV_H4Cells](https://github.com/MMV-Lab/mmv_h4cells) napari plugin. For more information, read the corresponding [README](https://github.com/MMV-Lab/mmv_h4cells/blob/main/README.md).

## Installation

## Installation

1. **Set up the environment**:

    - Install [Anaconda](https://www.anaconda.com/download/success).
    - Create a new environment:
        ```bash
        conda create --name mmv_h4cells_helper python=3.9
        conda activate mmv_h4cells_helper
        ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Optional: GPU support**:
    If you wish to use GPU for faster computation, follow the instructions provided [here](https://github.com/MouseLand/cellpose?tab=readme-ov-file#gpu-version-cuda-on-windows-or-linux) to install the GPU version of the required libraries.

## Usage

To execute the scripts, follow these steps:

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
    - The masks will be exported to the `results` folder and can be opened and further processed using napari and the `MMV_H4Cells` plugin.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.