import numpy as np
from pathlib import Path
from aicsimageio import AICSImage
from aicsimageio.writers import OmeTiffWriter
from tqdm import tqdm
from multiprocessing import Pool, cpu_count
import time

def process_cell(cell_id, cells, nuclei):
    cell_mask = cells == cell_id
    nuclei_in_cell = np.unique(nuclei[cell_mask])
    nuclei_in_cell = nuclei_in_cell[nuclei_in_cell != 0] 

    for nucleus_id in nuclei_in_cell:
        nucleus_mask = nuclei == nucleus_id
        if np.all(cell_mask[nucleus_mask]):
            return cell_id, cell_mask
    return None, None

def process_file(fn):
    nuclei_reader = AICSImage(fn)
    nuclei = nuclei_reader.get_image_data("YX")

    cells_reader = AICSImage(Path('data', 'cells', fn.name))
    cells = cells_reader.get_image_data("YX")

    cell_ids = np.unique(cells)[1:]

    result = np.zeros(cells.shape, dtype=np.uint16)  

    num_workers = min(int(cpu_count()*0.8), len(cell_ids)) 
    batch_size = 100  

    for i in range(0, len(cell_ids), batch_size):
        batch = cell_ids[i:i + batch_size]
        with Pool(num_workers) as pool:
            results = list(tqdm(pool.starmap(process_cell, [(cell_id, cells, nuclei) for cell_id in batch]), total=len(batch)))

        for cell_id, cell_mask in results:
            if cell_id is not None:
                result[cell_mask] = cell_id

    output_path = Path('results', fn.stem + '_merged.tif')
    OmeTiffWriter.save(result, output_path, dim_order_out="YX")

def main():
    fns = list(Path('data', 'nuclei').glob('*.tif*'))
    Path('results').mkdir(exist_ok=True, parents=True) # Create results folder if it doesn't exist
    
    for fn in tqdm(fns):
        start = time.time()
        process_file(fn)
        end = time.time()
        print(f"Processing {fn.name} took {int(end-start)} seconds")

if __name__ == '__main__':
    main()
