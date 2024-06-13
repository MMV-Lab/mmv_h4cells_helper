# Adapted from https://github.com/MouseLand/cellpose

from cellpose import core, io, models
from aicsimageio.writers import OmeTiffWriter
from pathlib import Path
from tqdm import tqdm
import time

path_raw_images = Path('data/raw')

use_GPU = core.use_gpu()
yn = ['NO', 'YES']
print(f'>>> GPU activated? {yn[use_GPU]}')

dir_raw = Path(path_raw_images)
savedir = Path(path_raw_images.parent, 'cells')
model_path = 'models/cells'

chan = 2 # 0 if grayscale, 1/2/3 if RGB, so 1 for red, 2 for green, 3 for blue
chan2 = 0
flow_threshold = 0.4
cellprob_threshold = 0

# declare model
model = models.CellposeModel(gpu=True, 
                             pretrained_model=model_path)

# run model on test images
filenames = sorted(path_raw_images.glob("*.tif*"))
for fn in tqdm(filenames):
    start = time.time()
    image = io.imread(fn)
    masks, _, _ = model.eval([image], channels=[chan, chan2])
    out_path = savedir / fn.name
    OmeTiffWriter.save(masks[0], out_path, dim_order="YX")                                  
    end = time.time()
    print(f"Processing {fn.name} took {int(end-start)} seconds (cells)")