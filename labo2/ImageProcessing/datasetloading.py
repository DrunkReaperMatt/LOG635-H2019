from pathlib import Path
import numpy as np

from labo2.ImageProcessing.imageprocess import process_image
from sklearn.utils import Bunch


# Load Ensemble (B) into dataset for validation
def load_ensemble(ensemble_path):
    image_dir = Path(ensemble_path)
    # Extract folders from main directory (..\EnsembleB\)
    folders = [directory for directory in image_dir.iterdir() if directory.is_dir()]
    # Categorize data sets according to the folder names
    categories = [folder.name for folder in folders]

    images = []
    flat_data = []
    target = []

    for i, direct in enumerate(folders):
        for file in direct.iterdir():
            # apply pre-processing on image
            img = process_image(str(file))
            flat_data.append(img.flatten())
            images.append(img)
            target.append(i)

    flat_data = np.array(flat_data)
    target = np.array(target)
    images = np.array(images)

    # return data set containing all cropped grayscale images
    return Bunch(data=flat_data,
                 target=target,
                 target_names=categories,
                 images=images)
