import rasterio
import cv2
import numpy as np
from pathlib import Path


def convert_tif_to_png(tif_path, png_path):
    with rasterio.open(tif_path, "r") as tif_file:
        # Convert to numpy arrays
        bands = tif_file.read()
        rgb = bands[:3, ...]
        rgb = np.moveaxis(rgb, 0, 2).astype(np.float32)
        cv2.imwrite(
            filename=str(png_path), img=cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
        )

if __name__ == '__main__':
    tifs_path = Path("PATH_TO_FOLDER")
    pngs_path = Path("SAVE_PATH")

    for tif_file in tifs_path.iterdir():
        png_name = tif_file.name.replace('.tif','.png')
        png_path = pngs_path / png_name
        convert_tif_to_png(tif_file, png_path)
