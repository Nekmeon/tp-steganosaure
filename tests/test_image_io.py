from steganosaure.image_io import load_image
from steganosaure.image_io import save_image
import pathlib
import numpy


original_image = pathlib.Path(__file__).parent / "images" / "size.png"
testing_image = pathlib.Path(__file__).parent / "images" / "size_bis.png"


def test_load_saved_image() -> None:
    o_image = load_image(original_image)
    save_image(o_image, testing_image)
    t_image = load_image(testing_image)
    numpy.testing.assert_array_equal(o_image, t_image)
