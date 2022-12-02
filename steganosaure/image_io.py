import pathlib
import numpy
from skimage import io, util


def load_image(image_path: pathlib.Path) -> numpy.ndarray:
    loaded_image = io.imread(image_path)
    converted_image = util.img_as_ubyte(loaded_image)
    return converted_image


# pathlib.Path.with_suffixes(".png")
def save_image(image: numpy.ndarray, image_path: pathlib.Path) -> None:
    io.imsave(image_path, image, plugin="pil", check_contrast=False)
